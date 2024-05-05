import subprocess

def retrain_rasa_model():
    # Run the Rasa training command using subprocess
    try:
        subprocess.run(["rasa", "train"])
        print("Rasa model retrained successfully.")
    except Exception as e:
        print(f"Error retraining Rasa model: {e}")

if __name__ == "__main__":
    # Call the retrain_rasa_model function when the script is executed directly
    retrain_rasa_model()
