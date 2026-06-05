import json

class PromptOptimizer:
    def __init__(self):
        self.styles = {
            "chibi": "chibi style, cute, oversized head, expressive eyes, vibrant colors, clean lineart, digital art, 8k resolution, detailed background",
            "cinematic": "cinematic lighting, photorealistic, dramatic shadows, 8k resolution, highly detailed, shot on 35mm lens, depth of field, masterpiece",
            "cyberpunk": "cyberpunk aesthetic, neon lighting, futuristic city, high tech, gritty textures, glowing elements, octane render, synthwave palette"
        }

    def optimize(self, core_idea, style_type="cinematic", aspect_ratio="16:9"):
        """Optimizes a raw concept into a structured AI prompt."""
        selected_style = self.styles.get(style_type.lower(), self.styles["cinematic"])
        
        optimized_prompt = {
            "core_subject": core_idea.strip(),
            "style_modifiers": selected_style,
            "technical_aspects": f"--ar {aspect_ratio} --v 6.0 --quality premium",
            "final_output": f"{core_idea.strip()}, {selected_style} --ar {aspect_ratio}"
        }
        return optimized_prompt

# Quick testing loop for the open-source community
if __name__ == "__main__":
    optimizer = PromptOptimizer()
    print("--- AI Prompt Optimizer Tool initialized ---")
    test_concept = "A mysterious cat sitting on a neon-lit cyberpunk rooftop"
    result = optimizer.optimize(test_concept, style_type="cyberpunk")
    print(json.dumps(result, indent=4))
