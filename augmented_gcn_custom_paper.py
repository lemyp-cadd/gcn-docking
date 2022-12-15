# -*- coding: utf-8 -*-
"""Augmented_GCN_custom_paper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eczpywuCgy8xhNz6-g_LkRijfWL1i4zi

# **Custom version of augmented_GCN for classification**

## Downloading necesary data
"""

# Set working directory 
from google.colab import drive
drive.mount('/content/drive')

images_dir = '/content/drive'

# Set working directory 
!git clone https://github.com/lemyp-cadd/gcn-docking.git

# Commented out IPython magic to ensure Python compatibility.
# %cd gcn-docking
!tar -Jxvf AID1478_train.tar.xz
!tar -Jxvf AID1478_test.tar.xz

"""## Making a conda enviroment to train the GCN"""

# Commented out IPython magic to ensure Python compatibility.
# %env PYTHONPATH = # /env/python

!wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.12.0-Linux-x86_64.sh
!chmod +x Miniconda3-py38_4.12.0-Linux-x86_64.sh
!./Miniconda3-py38_4.12.0-Linux-x86_64.sh -b -f -p /usr/local
!conda update conda

import sys
sys.path.append('/usr/local/lib/python3.8/site-packages')

!conda create -n myenv python=3.6

# Commented out IPython magic to ensure Python compatibility.
# %%bash
# eval "$(conda shell.bash hook)"
# conda activate myenv
# pip install matplotlib
# conda install ipykernel
#

# Commented out IPython magic to ensure Python compatibility.
# %%bash
# eval "$(conda shell.bash hook)"
# conda activate myenv
# pip install google-colab

# Commented out IPython magic to ensure Python compatibility.
# %%bash
# eval "$(conda shell.bash hook)"
# conda activate myenv
# pip install tensorflow-gpu==1.15

# Commented out IPython magic to ensure Python compatibility.
# %%bash
# eval "$(conda shell.bash hook)"
# conda activate myenv
# conda install scikit-learn

# Commented out IPython magic to ensure Python compatibility.
# %%bash
# source activate myenv
# python -m ipykernel install --user --name myenv --display-name "Python (myenv)"

!source activate myenv && conda env list

# Commented out IPython magic to ensure Python compatibility.
# %%bash
# source activate myenv
# 
# python
# import sys
# import numpy as np
# from google.colab import files
# # some simple python commands
# sys.path.append('/usr/local/lib/python3.6/site-packages')
# print(sys.path)
# 
# print("Python version")
# print(sys.version)
#

"""## Training GCN"""

#%cd ../
#!rm -r gcn-docking
#!ls
#!pip uninstall tensorflow -y

# Commented out IPython magic to ensure Python compatibility.
# %%bash
# source activate myenv
# 
# python
# import sys
# # some simple python commands
# sys.path.append('/usr/local/lib/python3.6/site-packages')
# print(sys.path)
# 
# print("Python version")
# print(sys.version)
# import tensorflow as tf
# print(tf.__version__)
# import numpy as np
# from sklearn.metrics import accuracy_score
# from sklearn.metrics import roc_curve
# from sklearn.metrics import roc_auc_score
# from google.colab import files
# 
# 
# import tensorflow.compat.v1 as tf
# tf.disable_v2_behavior()
# 
# # Set FLAGS for environment setting / hyperparameters 
# method = 'GCN+a+g'
# prop = 'activity' ### CHANGED ###
# database = 'AID1478_train'
# num_layer = 5 # number of convolutional layers 
# epoch_size = 40
# learning_rate = 0.001
# decay_rate = 0.95
# numDB = 1   ### This is the train num_Db ###
# test_numDB = 4
# unit_len = 10000
# 
# flags = tf.app.flags
# 
# FLAGS = flags.FLAGS
# for name in list(flags.FLAGS):
#     delattr(flags.FLAGS,name)
# 
# flags.DEFINE_string('model', method, 'GCN, GCN+a, GCN+g, GCN+a+g')
# flags.DEFINE_string('output', prop, '')
# flags.DEFINE_string('loss_type', 'CrossEntropy', 'Options : MSE, CrossEntropy, Hinge')  ### CHANGED ###  
# flags.DEFINE_string('database', database, 'Options : ZINC, ZINC2')  ### Using MSEr 
# flags.DEFINE_string('optimizer', 'Adam', 'Options : Adam, SGD, RMSProp')
# flags.DEFINE_string('readout', 'atomwise', 'Options : atomwise, graph_gather')
# flags.DEFINE_integer('latent_dim', 512, 'Dimension of a latent vector for autoencoder')
# flags.DEFINE_integer('num_layers', num_layer, '# of hidden layers')
# flags.DEFINE_integer('epoch_size', epoch_size, 'Epoch size')
# flags.DEFINE_integer('batch_size', 100, 'Batch size')
# flags.DEFINE_integer('save_every', 1000, 'Save every')
# flags.DEFINE_float('learning_rate', learning_rate, 'Batch size')
# flags.DEFINE_float('decay_rate', decay_rate, 'Batch size')
# flags.DEFINE_integer('num_DB', numDB, '')
# flags.DEFINE_integer('unitLen', unit_len, '')
# tf.app.flags.DEFINE_string('f', '', 'kernel')
# 
# modelName = FLAGS.model + '_' + str(FLAGS.num_layers) + '_' + FLAGS.output + '_' + FLAGS.readout + '_' + str(FLAGS.latent_dim) + '_' + FLAGS.database
# 
# print("model Name: ", modelName)
# 
# # Build the model
# import warnings
# warnings.simplefilter(action='ignore', category=FutureWarning)
# from Graph2Property_mod import Graph2Property  ### CHANGED ###
# tf.reset_default_graph()
# tf.set_random_seed(1234)	# For reproducibility purposes, a random seed was set
# model = Graph2Property(FLAGS)
# 
# # restore the model if available 
# path='save/'+modelName+'.ckpt'
# try: 
#   model.restore(path)
# except Exception as e: print(e)
# 
# # Train the model 
# 
# import train_mod 
# train_cost, test_cost = train_mod.training(model, FLAGS, modelName)
# 
# # plot cost versus epoch 
# from matplotlib import pyplot
# images_dir = '/content/drive/My Drive'
# 
# epochs = np.arange(1, FLAGS.epoch_size+1, 1)
# 
# pyplot.plot(epochs,train_cost, label='train')
# pyplot.plot(epochs,test_cost, label='valid')
# pyplot.xlabel('epoch')
# pyplot.ylabel('cross entropy')
# pyplot.legend(loc='upper right', fontsize=13, frameon=False)
# pyplot.savefig(f"{images_dir}/cost_vs_epoch.png")
# #files.download("cost_vs_epoch.png")
# #pyplot.show() 
# pyplot.close()
# 
# # Eval
# from eval import train_valid_split
# from eval import pred_batches
# from eval import loadTest
# 
# # load tran valid and test 
# train_set, valid_set = train_valid_split(model, FLAGS, modelName)
# 
# test_database = 'AID1478_test'
# test_set = loadTest(model, FLAGS, modelName, test_database, test_numDB)
# 
# # extract predictions out of batches 
# Preds_train_set = pred_batches(model, train_set, FLAGS)
# Preds_valid_set = pred_batches(model, valid_set, FLAGS)
# Preds_test_set = pred_batches(model, test_set, FLAGS)
# 
# # calculate accuracy score
# accuracy = accuracy_score(valid_set[2], Preds_valid_set.round())
# print ("valid accuracy: ", accuracy)
# 
# accuracy = accuracy_score(test_set[2], Preds_test_set.round())
# print ("test accuracy: ", accuracy)
# 
# # calculate auc score & plot roc curve 
# fpr, tpr, _ = roc_curve(valid_set[2], Preds_valid_set)
# auc = roc_auc_score(valid_set[2], Preds_valid_set)
# print ("valid AUC: ", auc)
# 
# pyplot.plot(fpr, tpr, marker='.', label='AUC = {:0.3f}'.format(auc))
# pyplot.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
# # axis labels
# pyplot.xlabel('False Positive Rate')
# pyplot.ylabel('True Positive Rate')
# pyplot.legend(loc='lower right', fontsize=13, frameon=False)
# # save the plot
# pyplot.savefig('roc_curve_valid.png')
# pyplot.close()
# 
# fpr, tpr, _ = roc_curve(test_set[2], Preds_test_set)
# auc = roc_auc_score(test_set[2], Preds_test_set)
# print ("test AUC: ", auc)
# 
# pyplot.plot(fpr, tpr, marker='.', label='AUC = {:0.3f}'.format(auc))
# pyplot.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
# # axis labels
# pyplot.xlabel('False Positive Rate')
# pyplot.ylabel('True Positive Rate')
# pyplot.legend(loc='lower right', fontsize=13, frameon=False)
# #pyplot.show()
# # save the plot
# pyplot.savefig(f"{images_dir}/roc_curve_test.png")