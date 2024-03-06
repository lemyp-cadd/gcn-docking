#  Graph neural networks and molecular docking as two complementary approaches for virtual screening: a case study on Cruzain 

-----------------------------------------------------------------------------------------------------------------------------------------

## Authors: 
### Gómez Chávez, José Leonardo; Luchi, Adriano; Villafañe, Roxana; Conti, Germán;Perez, Rafael; Angelina, Emilio Luis; Peruchena, Nélida María


*Laboratorio de Estructura Molecular y Propiedades (LEMyP) - IQUIBA-NEA, Universidad Nacional del Nordeste, CONICET, FACENA, Av. Libertad
5470, Corrientes 3400, Argentina.*


------------------------------------------------------------------------------------------------------------------------------------------
This repository provides information on training the Graph convolutional network implemented in the paper "Graph Neural Networks and Molecular Docking as Two Complementary Approaches for Virtual Screening: A Cruzain Case Study".

In this work, we leveraged activity data from a high-throughput quantitative screen (HTS) of ~200K compounds against Cruzain (Cz) to retrospectively evaluate the ability of a graphical convolutional network (GCN) to prioritize active compounds from the data set.

The data set used corresponds to the data set created by Ferreira, R. S. in "Complementarity between a Docking and a High-Throughput Screen in Discovering New Cruzain Inhibitors" (J. Med. Chem. 2010, 53 (13), 4891-4905 , DOI: 10.1021/jm100488w).
This data set is commonly known as the AID 1478 data set and is available at https://pubchem.ncbi.nlm.nih.gov/bioassay/1478#section=Data-Table

All the files needed to train the Graph convolutional network are available here.
You must follow the steps in the usage section. Inside the notebooks are all the libraries and packages needed for network training. You don't need to edit anything.

![gcn-architecture](https://github.com/lemyp-cadd/gcn-docking/blob/main/cover%20fig.png)

#   Usage
------------------------------------------------------------------------------------------------------------------------------------------
The graph convolutional network used in this repository is based on the work of https://github.com/SeongokRyu/augmented-GCN, which in turn is built upon https://github.com/HIPS/neural-fingerprint. The hyperparameter tuning and overall architecture of the standard and augmented GCNs remain the same as in the original implementation by Ryu et al. (2018), with the exception of the last layer activation function and the loss function, which were modified for a classification task.

All notebooks have links to Google drive colaboratory. You just need to click on the "open in Colab" tab and then create a copy on your own google drive or if you prefer, you can clone the entire github repository and work with it.

#  1 - Clone github repository
It can be downloaded in two ways: 

## github website  

https://github.com/lemyp-cadd/gcn-docking/archive/refs/heads/main.zip

## linux terminal
If you do not have github installed on your computer, you should install this first in your linux terminal

 ```apt-get install git```
 
 then use git clone
 
 ```git clone https://github.com/lemyp-cadd/gcn-docking.git```

#  2 - Convert smiles files to graph inputs
Open the Google Collaborative file called "smiles_to_graph.ipynb" and click on the "open in Colab" tab at the top. Create a copy on your google drive and follow the instructions. Inside it is an example for turning smiley molecules into graphics to be used as inputs to the GCN.

#  3 - Training 
Open the Google Collaborative file called "Augmented_GCN_custom_github.ipynb" and click on the "open in Colab" tab at the top. Create a copy on your google drive and follow the instructions. Inside it is the GCN training example used in this work.

## Work is underway to migrate the code to TensorFlow 2. Therefore, this version is functional but will be replaced soon.
