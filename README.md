#  Graph neural networks and molecular docking as two complementary approaches for virtual screening: a case study on Cruzain 

-----------------------------------------------------------------------------------------------------------------------------------------

Authors: 
Luchi, Adriano; Gómez Chávez, José Leonardo; Villafañe, Roxana; Conti, Germán;Perez, Rafael; Angelina, Emilio Luis; Peruchena, Nélida María


*Laboratorio de Estructura Molecular y Propiedades (LEMyP) - IQUIBA-NEA, Universidad Nacional del Nordeste, CONICET, FACENA, Av. Libertad
5470, Corrientes 3400, Argentina.*


------------------------------------------------------------------------------------------------------------------------------------------

This repository provides information about the training of the Graph convolutional network implemented in the work "Graph neural networks and molecular docking as two complementary approaches for virtual screening: a case study on Cruzain". 

The dataset used in this work corresponds to the dataset used by Ferreira, R. S. in "Complementarity between a Docking and a High-Throughput Screen in Discovering New Cruzain Inhibitors" (J. Med. Chem. 2010, 53 (13), 4891-4905, DOI: 10.1021/jm100488w). This dataset is commonly referred to as the AID 1478 dataset.

All the files needed to train the Graph convolutional network are available here.
You need to follow the steps in the usage section. Inside the notebooks are all the necessary libraries and packages for network training. You do not need to edit anything.

![gcn-architecture](https://github.com/lemyp-cadd/gcn-docking/blob/main/cover%20fig.png)

#   Usage
------------------------------------------------------------------------------------------------------------------------------------------
The graph convolutional network used in this repository is based on the work of https://github.com/SeongokRyu/augmented-GCN, which in turn is built upon https://github.com/HIPS/neural-fingerprint. The hyperparameter tuning and overall architecture of the standard and augmented GCNs remain the same as in the original implementation by Ryu et al. (2018), with the exception of the last layer activation function and the loss function, which were modified for a classification task.

#  1 - Clone github repository
It can be downloaded directly from the github website or through the linux terminal

https://github.com/lemyp-cadd/gcn-docking/archive/refs/heads/main.zip

## Install github on linux
 ```apt-get install git```
 
 then use git clone
 
 ```git clone https://github.com/lemyp-cadd/gcn-docking.git```

#  2 - Convert smiles files to graph inputs at a database folder
Upload the Google collaborative file named "smiles_to_graph.ipynb" to your Google Drive and follow the instructions. Inside it is an example for turning smiley molecules into graphics to be used as inputs to the GCN.

#  3 - Training 
Upload the Google collaborative file named "Augmented_GCN_custom_github.ipynb" to your Google Drive and follow the instructions. Inside it is the GCN training example used in this work.


