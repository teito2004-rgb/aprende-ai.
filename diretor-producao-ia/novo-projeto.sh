#!/usr/bin/env bash
# Uso: ./novo-projeto.sh nome-do-projeto "Nome do Cliente"
set -euo pipefail
cd "$(dirname "$0")"
[ $# -ge 1 ] || { echo 'Uso: ./novo-projeto.sh nome-do-projeto "Cliente"'; exit 1; }
slug="$1"; cliente="${2:-}"
if ! [[ "$slug" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
  echo "Nome inválido: use só letras minúsculas sem acento, números e hífens (ex.: campanha-verao)."; exit 1
fi
cliente="${cliente//|/-}"   # "|" quebraria as tabelas
dest="projetos/$slug"
[ -e "$dest" ] && { echo "Já existe: $dest"; exit 1; }
cp -r projetos/_modelo-projeto "$dest"
sed -i "s/PROJETO/$slug/g" "$dest"/*.md

# awk com variáveis de ambiente: o nome do cliente entra literalmente, sem escapes
export CLIENTE="$cliente" LINHA="| $slug | $cliente | | 🟦 Briefing | Preencher briefing | | [abrir](projetos/$slug/briefing.md) |"
tmp=$(mktemp)
awk '$0 == "- **Cliente:** " && ENVIRON["CLIENTE"] != "" { print "- **Cliente:** " ENVIRON["CLIENTE"]; next } { print }' \
  "$dest/briefing.md" > "$tmp" && cat "$tmp" > "$dest/briefing.md"
awk 'index($0, "| _(nenhum ainda") == 1 { next }
     { print }
     !feito && $0 == "|---|---|---|---|---|---|---|" { print ENVIRON["LINHA"]; feito = 1 }' \
  painel.md > "$tmp" && cat "$tmp" > painel.md
rm -f "$tmp"
echo "Projeto criado em $dest e adicionado ao painel."
