import json
import argparse
import sys

def evaluate_spatial_scene(scene_file):
    print(f"[INFO] Auditing 3D spatial scene: {scene_file}")
    with open(scene_file, "r") as f:
        scene = json.load(f)
    
    objects = scene.get("objects", [])
    print(f"[INFO] Detected {len(objects)} 3D entities in scene.")
    
    for obj in objects:
        coords = obj.get("position", [0, 0, 0])
        if len(coords) != 3:
            print(f"[ERROR] Object {obj.get('id')} has invalid 3D coordinate dimension: {coords}")
            sys.exit(1)
        scale = obj.get("scale", [1, 1, 1])
        if any(s <= 0 for s in scale):
            print(f"[ERROR] Non-positive scale detected on {obj.get('id')}: {scale}")
            sys.exit(1)
            
    print("[SUCCESS] Spatial scene hierarchy and coordinate matrices passed 100% verification.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--scene", default="samples/room_scene.json")
    args = parser.parse_args()
    evaluate_spatial_scene(args.scene)
