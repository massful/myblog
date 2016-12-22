#!/usr/bin/env python
#coding=utf-8

import os 
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  SECRET_KEY = os.environ.get('Flask_secret_key') or 'ni cai a'
  SQLALCHEMY_COMMIT_ON_TEARDOWN = True

  @staticmethod
  def init_app(app):
    pass

class DevelopmentConfig(config):
  DEBUG = True

