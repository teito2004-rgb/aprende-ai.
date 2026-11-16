#!/usr/bin/env bash
# Uso: ./novo-projeto.sh nome-do-projeto "Nome do Cliente"
set -euo pipefail
cd "$(dirname "$0")"
[ $# -ge 1 ] || { echo 'Uso: ./novo-projeto.sh nome-do-projeto "Cliente"'; exit 1; }
slug="$1"; cliente="${2:-}"
dest="projetos/$slug"
[ -e "$dest" ] && { echo "Já existe: $dest"; exit 1; }
cp -r projetos/_modelo-projeto "$dest"
sed -i "s/PROJETO/$slug/g" "$dest"/*.md
[ -n "$cliente" ] && sed -i "s/^- \*\*Cliente:\*\* $/- **Cliente:** $cliente/" "$dest/briefing.md"
linha="| $slug | $cliente | | 🟦 Briefing | Preencher briefing | | [abrir](projetos/$slug/briefing.md) |"
sed -i "/^| _(nenhum ainda/d" painel.md
sed -i "/^|---|---|---|---|---|---|---|$/a $linha" painel.md
echo "Projeto criado em $dest e adicionado ao painel."
