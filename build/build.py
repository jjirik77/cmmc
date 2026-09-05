#!/usr/bin/env python3
import os, sys, importlib
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import render

def collect():
    mods, L = ["content_a", "content_b", "content_c"], []
    for m in mods:
        try:
            mod = importlib.import_module(m)
        except ModuleNotFoundError:
            continue
        for name in sorted([n for n in dir(mod) if n.startswith("L") and n[1:].isdigit()],
                           key=lambda n: int(n[1:])):
            L.append(getattr(mod, name))
    return L

def main():
    L = collect()
    for lesson in L:
        p = os.path.join(OUT, lesson["file"])
        with open(p, "w", encoding="utf8") as f:
            f.write(render.lesson_page(lesson, L))
        print("  lesson :", lesson["file"], f"{os.path.getsize(p)//1024} KB")
    with open(os.path.join(OUT, "03_manuscript.md"), "w", encoding="utf8") as f:
        f.write(render.manuscript(L))
    print("  manuscript: 03_manuscript.md")
    try:
        import index as idx
        with open(os.path.join(OUT, "index.html"), "w", encoding="utf8") as f:
            f.write(idx.build(L))
        print("  index  : index.html")
    except ModuleNotFoundError:
        print("  index  : (index.py not present yet)")
    try:
        import tools as T
        for fname, htmlsrc in T.build_all():
            with open(os.path.join(OUT, fname), "w", encoding="utf8") as f:
                f.write(htmlsrc)
            print("  tool   :", fname)
    except ModuleNotFoundError:
        print("  tools  : (tools.py not present yet)")
    print(f"\nBuilt {len(L)} lesson page(s) into {OUT}")

if __name__ == "__main__":
    main()
