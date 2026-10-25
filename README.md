# Spatial AI Scene Evaluation & 3D Reconstruction Pipeline

An automated quality assurance and evaluation suite for assessing frontier LLM-generated 3D spatial scenes (Three.js / WebGL), primitive bounding boxes, and GLB asset topologies.

---

## 🎯 Overview
Frontier vision-language models often generate synthetic HTML/Three.js spatial scenes with geometric errors, coordinate misalignments, or invalid camera transformation matrices. This toolkit provides programmatic checks to audit spatial reasoning outputs.

---

## 🛠️ Modules
- **Coordinate Matrix Validation:** Verifies scene camera projection, view matrices, and bounding volumes.
- **Topology & Mesh Auditing:** Detects non-manifold geometry, inverted normals, and high-poly bottlenecks.
- **Asset Upgrade Pipeline:** Converts primitive geometric proxies into production-ready PBR GLB assets.

---

## 🚀 Usage
```bash
python src/evaluate_spatial_scene.py --scene samples/room_scene.json
```
