# -*- coding: utf-8 -*-

from nnet import load_model
from predict import separate_sources


def main():

    model = load_model('model')
    
    separate_sources('mixed.wav', model, 2, 'out')


if __name__ == "__main__":
    main()
