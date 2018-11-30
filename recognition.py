import numpy as np # Import for numpy
import keras as kr # Import for keras, check notebook for details on how to install 
import gzip # import for gzip for handling files
import matplotlib.pyplot as plt # import for making plots 
import sklearn.preprocessing as pre # # Import for sklearn, for encoding categorical variables.
from keras.models import model_from_json # importing json for keras 

#print ("keras version: " + kr.__version__) # outputs the keras version number you have installed, used to see if everything is working fine

def NeuralNetwork() :
    model = kr.models.Sequential() # create a neural network first and then build it by layers

    # Adds hidden layer with 100 neurons 
    model.add(kr.layers.Dense(units=600, activation='linear', input_dim=784))
    model.add(kr.layers.Dense(units=400, activation='relu'))
# three neuron output layer.
    model.add(kr.layers.Dense(units=10, activation='softmax'))

# Build the graph.
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    with gzip.open('MNISTdata/train-images-idx3-ubyte.gz', 'rb') as f: # opens zipped training images folder
     trainimg = f.read()

    with gzip.open('MNISTdata/train-labels-idx1-ubyte.gz', 'rb') as f:  # opens zipped train labels folder 
     trainlbl = f.read()

    trainimg = ~np.array(list(trainimg[16:])).reshape(60000, 28, 28).astype(np.uint8) / 255.0 # division by 255 
    trainlbl =  np.array(list(trainlbl[ 8:])).astype(np.uint8) # sets the trainlbls

    inputs = trainimg.reshape(60000, 784) # reshapes
    # encodes the bytes to binary 
    encoder = pre.LabelBinarizer()
    encoder.fit(trainlbl)
    outputs = encoder.transform(trainlbl)

    #print(trainlbl[0], outputs[0]) this will test to make sure the concoder worked

    model.fit(inputs, outputs, epochs=10, batch_size=100) # fits the model with the inputs and outputs, 10 epochs are used to see how tests differentate from eachother

print ("keras version: " + kr.__version__)

def Menu():

    
    
    print("Welcome to the Digit Recognition Script! ") # Headers and decorators 
    print("Enter 1 to test the network with the MNIST dataset ") # Option to allow the user to choose an image for recognition testing 
    print("Enter 2 to test the network with a choosen image ") # Option to allow the user to choose an image for recognition testing 
    print("Enter 3 to exit the program ") # Exits the program 

    choice = input ("Input: ") # Allows the user to enter his/her options

    if choice == "1": # if choice one is enterted the model will be tested with the MNIST dataset
        NeuralNetwork()
    
    elif choice == "3":
        SystemExit # exits the system 
        
    
def main(): # main function 
   Menu()



if __name__ == '__main__': # handles the main function and brings to user to the menu on start up 
    main()  
#print ("keras version: " + kr.__version__) # outputs the keras version number you have installed, used to see if everything is working fine
#def sayhello() : 
 #   print ("this is cool")
  #  print ("Hello python")