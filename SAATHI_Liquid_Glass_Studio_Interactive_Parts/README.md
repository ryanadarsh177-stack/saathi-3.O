# SAATHI Liquid Glass Design Studio

A two-page Streamlit app with an iOS-inspired frosted glass interface and an interactive pendant assembly workbench.

## Pages
1. **Components** — nine pendant components with selectable explanations.
2. **Assembly Lab** — click-to-install animated component assembly, exploded/assembled views, drag-to-rotate, scroll-to-zoom, auto-build, reset, component inspection and simulated SOS signal pathway.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud
Push `app.py`, `requirements.txt`, and `README.md` to a GitHub repository. Create a new Streamlit app, select the repository, and set the main file path to `app.py`.

## Rendering fix
The viewport animation loop now continues while the Assembly tab is hidden, then resizes and paints as soon as the tab is opened. This fixes the blank canvas caused by initializing a canvas inside a hidden tab. Installing a component now animates it into the assembled pendant position.

## Engineering note
This is an interactive schematic visualization, not a validated electronics simulator or manufacturing CAD model. Component geometry and internal placement are illustrative. The SOS trace is simulated and does not transmit RF or contact emergency services.

## Component labels and animated previews
- Every part is named in the component library and has a numbered label in the pendant viewport.
- Selecting a component opens its description and a looping, GIF-like animated preview of its role. The Replay button restarts the preview.
- In the Assembly Lab, tapping a part row selects it and starts its attachment animation; the + button does the same. Tap an installed component in the viewport to inspect it.
- These previews are lightweight browser animations rather than embedded video files, so they work without hosting separate GIF/video assets.
