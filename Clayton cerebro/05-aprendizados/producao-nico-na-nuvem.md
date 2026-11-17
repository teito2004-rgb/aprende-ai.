# Produzir o Nico Explica numa sessão de nuvem do Claude Code
Data: 2026-11-17 · Contexto: episódio #26 (palavra repetida) · Status: confirmado (exceto download da voz)

## Em uma frase
Dá para fazer quase tudo de graça na nuvem (pesquisa, roteiro, vídeo HyperFrames, som por código); o gargalo é baixar a voz do ElevenLabs.

## O que funciona
- HyperFrames 0.9.61 via `npx` renderiza aqui (Chromium da máquina, modo screenshot). Inter é baixada sozinha. GSAP: usar cópia local (`npm pack gsap@3.15.0`), o CDN é bloqueado. — teste 17/11
- Voz: `creative_add_flow_node` no fluxo "Nico Explica — Lote 15 a 19" + `creative_run_flow_nodes` com `estimate_only` primeiro. Voz "Nico — Voz original v1" = `8m2JBfcV7wt9QcPYdIrr`, eleven_v4, estabilidade 0,65, similaridade 0,75, `language_code: pt`. ~900 caracteres ≈ 903 créditos (≈ US$ 0,16), 58,9 s.
- Temas já feitos: ver os nós do fluxo do lote (15 cômodo, 16 bebê, 17 déjà vu, 18 atenção, 19 bocejo, chiclete musical, 21 mudança, 22 cócegas, 23 dedo anelar, 24 ponta da língua, 25 estalar os dedos). Ler antes de escolher pauta.
- Pipeline do projeto: `cenas.json` → `tools/gerar.py` (cenas, legendas, SRT) → `tools/finalizar.py` (pausas reais com silencedetect, som com `som_codigo.py`, mix −16 LUFS) → `hyperframes render`.
- Subagentes: Nico (pesquisa via WebSearch) e Chico (revisão) funcionam bem; mandar mudança de pauta cedo.

## O que não funciona / armadilhas
- Rede limitada: PubMed, Wikipedia, sites em geral bloqueados para curl; pesquisa só por WebSearch.
- O arquivo da voz fica em `elevenlabsusercontent.com` (link assinado). Liberar o host no ambiente não basta: o classificador de permissões bloqueou o download. Solução pendente com o Clayton (regra de permissão ou ele baixa e envia o MP3).
- Escolhi "bocejo" sem checar: já era o #19. Sempre ler o fluxo do lote antes.

## Próxima vez
- Checar temas no fluxo do lote antes da pauta.
- Resolver o download antes de gastar crédito na voz.
