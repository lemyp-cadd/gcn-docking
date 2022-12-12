from train_mod import loadInputs
import numpy as np


# extract predictions out of batches 
def pred_batches(model, dataset, FLAGS):
    num_batches = int(dataset[0].shape[0]/FLAGS.batch_size)
    Pred_list = []
    for _iter in range(num_batches):
        A_batch = dataset[0][_iter*FLAGS.batch_size:(_iter+1)*FLAGS.batch_size]
        X_batch = dataset[1][_iter*FLAGS.batch_size:(_iter+1)*FLAGS.batch_size]
        P_batch = dataset[2][_iter*FLAGS.batch_size:(_iter+1)*FLAGS.batch_size]
        pred_batch = model.predict(A_batch, X_batch)
        Pred_list.append(pred_batch)
    return np.hstack(Pred_list).flatten()


def train_valid_split(model, FLAGS, modelName):
    batch_size = FLAGS.batch_size
    num_DB = FLAGS.num_DB
    unitLen = FLAGS.unitLen
    Xs_train = []
    As_train = []
    Props_train = []
    Xs_valid = []
    As_valid = []
    Props_valid = []
    total_iter = 0
    for i in range(0,num_DB):
        _graph, _property = loadInputs(FLAGS, i, modelName, unitLen)
        num_batches = int(_graph[0].shape[0]/batch_size)
        for _iter in range(num_batches):
            total_iter += 1
            A_batch = _graph[0][_iter*FLAGS.batch_size:(_iter+1)*FLAGS.batch_size]
            X_batch = _graph[1][_iter*FLAGS.batch_size:(_iter+1)*FLAGS.batch_size]
            P_batch = _property[_iter*FLAGS.batch_size:(_iter+1)*FLAGS.batch_size]
            if total_iter % 5 != 0:
                # Training
                As_train.append(A_batch)
                Xs_train.append(X_batch)
                Props_train.append(P_batch)
            elif total_iter % 5 == 0:
                # Test 
                As_valid.append(A_batch)
                Xs_valid.append(X_batch)
                Props_valid.append(P_batch)
    return (np.concatenate(As_train), np.concatenate(Xs_train), np.concatenate(Props_train)), (np.concatenate(As_valid), np.concatenate(Xs_valid), np.concatenate(Props_valid))

def loadTest(model, FLAGS, modelName, database, test_numDb):
    FLAGS.database = database
    batch_size = FLAGS.batch_size
    num_DB = test_numDb
    unitLen = FLAGS.unitLen
    Xs_test = []
    As_test = []
    Props_test = []
    for i in range(0,num_DB):
        _graph, _property = loadInputs(FLAGS, i, modelName, unitLen)
        num_batches = int(_graph[0].shape[0]/batch_size)
        for _iter in range(num_batches):
            A_batch = _graph[0][_iter*FLAGS.batch_size:(_iter+1)*FLAGS.batch_size]
            X_batch = _graph[1][_iter*FLAGS.batch_size:(_iter+1)*FLAGS.batch_size]
            P_batch = _property[_iter*FLAGS.batch_size:(_iter+1)*FLAGS.batch_size]
            As_test.append(A_batch)
            Xs_test.append(X_batch)
            Props_test.append(P_batch)
    return (np.concatenate(As_test), np.concatenate(Xs_test), np.concatenate(Props_test))
