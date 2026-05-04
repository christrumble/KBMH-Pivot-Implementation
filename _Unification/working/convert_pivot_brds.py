"""Convert all Pivot BRD docx files to markdown for synthesis work.

Drops outputs in _Unification/working/pivot-brds-md/{ModuleName}.md
"""
from pathlib import Path
import mammoth
import re

REPO = Path(__file__).resolve().parents[2]
OUT_DIR = REPO / "_Unification" / "working" / "pivot-brds-md"
OUT_DIR.mkdir(parents=True, exist_ok=True)

def module_name_from_path(docx_path: Path) -> str:
    # path: <repo>/<Module>/Pivot/4 BRD/<file>.docx
    parts = docx_path.relative_to(REPO).parts
    return parts[0].replace(" ", "_")

def convert(docx_path: Path) -> Path:
    with open(docx_path, "rb") as f:
        result = mammoth.convert_to_markdown(f)
    md = result.value
    # Mammoth produces tight markdown; normalize trailing whitespace and empty lines
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    out = OUT_DIR / f"{module_name_from_path(docx_path)}.md"
    header = f"# Pivot BRD — {module_name_from_path(docx_path).replace('_', ' ')}\n\n_Source: `{docx_path.relative_to(REPO)}`_\n\n---\n\n"
    out.write_text(header + md, encoding="utf-8")
    if result.messages:
        warnings_path = OUT_DIR / f"{module_name_from_path(docx_path)}.warnings.txt"
        warnings_path.write_text("\n".join(str(m) for m in result.messages))
    return out

def main():
    docx_files = sorted(REPO.glob("*/Pivot/4 BRD/*.docx"))
    print(f"Found {len(docx_files)} Pivot BRD docx files")
    for d in docx_files:
        out = convert(d)
        size = out.stat().st_size
        print(f"  {d.parts[-4]:32s} -> {out.name}  ({size:,} bytes)")

if __name__ == "__main__":
    main()
