import numpy as np # Import for numpy
import keras as kr # Import for keras, check notebook for details on how to install 
import gzip # import for gzip for handling files
import matplotlib.pyplot as plt # import for making plots 
import sklearn.preprocessing as pre # # Import for sklearn, for encoding categorical variables.
from keras.models import model_from_json # importing json for keras 

#print ("keras version: " + kr.__version__) # outputs the keras version number you have installed, used to see if everything is working fine

def NeuralNetwork() :
    model = kr.models.Sequential() # create a neural network first and then build it by layers

    # Add a hidden layer with 1000 neurons and an input layer with 784.
    model.add(kr.layers.Dense(units=600, activation='linear', input_dim=784))
    model.add(kr.layers.Dense(units=400, activation='relu'))
# Add a three neuron output layer.
    model.add(kr.layers.Dense(units=10, activation='softmax'))

# Build the graph.
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    with gzip.open('MNISTdata/train-images-idx3-ubyte.gz', 'rb') as f:
     trainimg = f.read()

    with gzip.open('MNISTdata/train-labels-idx1-ubyte.gz', 'rb') as f:
     trainlbl = f.read()

     print ("keras version: " + kr.__version__)

def Menu():

    
    
    print("Welcome to the Digit Recognition Script!") # Headers and decorators 
    print("Enter 1 to FEATURE COMING SOON") # Option to allow the user to choose an image for recognition testing 
    print("Enter 2 to exit the program") # Exits the program 

    choice = input ("Please make a choice: ") # Allows the user to enter his/her options

    if choice == "2": # if choice 2 is entered user exits program 
        SystemExit
    
def main(): # main function 
   NeuralNetwork()



if __name__ == '__main__': # handles the main function and brings to user to the menu on start up 
    main()  
#print ("keras version: " + kr.__version__) # outputs the keras version number you have installed, used to see if everything is working fine
#def sayhello() : 
 #   print ("this is cool")
  #  print ("Hello python")