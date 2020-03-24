'''
Load pretrain models and create a tensorflow session to run them

'''
import tensorflow as tf


class FaceRecGraph(object):
    def __init__(self):
        '''
            There'll be more to come in this class
        '''
        self.graph = tf.Graph();
