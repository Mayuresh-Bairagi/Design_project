import os
import base64
from dotenv import load_dotenv
from groq import Groq
from fastapi import HTTPException

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("groq_key")

class GroqModel:
    def __init__(self):
        self.model_name = "meta-llama/llama-4-scout-17b-16e-instruct"
        self.client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        self.suggestion_prompt = """
            Analyze the image of this fruit crop and provide 5 actionable suggestions to help the farmer improve both crop yield and market readiness. 
            Consider visual factors such as fruit size, ripeness, color uniformity, leaf health, signs of pests or diseases, and overall plant condition. 
            Your suggestions should focus on practices that can increase productivity and also enhance the visual appeal and quality of the fruit for better market value. 
            Include tips related to pruning, fertilization, irrigation, pest control, harvesting time, and post-harvest handling.
            only give the suggestions, do not give any other information.
            Do not include any disclaimers or additional context.
            Do not repeat the question.
            Do not include any greetings or salutations.
            give only this 5 suggestions in a list format.
            1.
            2.
            3.
            4.
            5.
        """

    def get_image_base64(self, image_path):
        try:
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode("utf-8")
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail="Image file not found.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error reading image: {str(e)}")

    def get_suggestions(self, image_path: str):
        image_base64 = self.get_image_base64(image_path)

        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": self.suggestion_prompt},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{image_base64}",
                                },
                            },
                        ],
                    }
                ],
                model=self.model_name,
            )

            response_suggestions = chat_completion.choices[0].message.content
            bullet_points = [line.strip() for line in response_suggestions.split("\n") if line.strip()]
            return {"response": bullet_points}

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Groq API error: {str(e)}")
