from gtts import gTTS

# Define the text you want to convert to speech
text = '''The 5-fold in the prostratecancerclahe5folds dataset refers to the 5-fold cross-validation scheme used to split the dataset. In 5-fold cross-validation, the dataset is randomly divided into 5 equal-sized folds. One fold is used as the test set, and the remaining 4 folds are used to train the model. This process is repeated 5 times, with each fold being used as the test set once.

5-fold cross-validation is a popular method for evaluating machine learning models because it provides a more robust estimate of the model's generalization performance than a single train-test split. This is because the model is evaluated on a variety of different test sets, each of which represents a different subset of the data.

The 5-fold cross-validation scheme used in the prostratecancerclahe5folds dataset ensures that each image in the dataset is used for training and testing exactly once. This helps to reduce the risk of overfitting and provides a more accurate estimate of the model's performance on unseen data.

I hope this explanation is helpful. Please let me know if you have any other questions.'''

# Create a gTTS object
tts = gTTS(text)

# Save the audio to an MP3 file
output_file = "output.mp3"
tts.save(output_file)

print(f"Audio saved to {output_file}")
