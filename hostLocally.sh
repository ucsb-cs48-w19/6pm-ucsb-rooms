#!/bin/bash
gunicorn3 -w 4 -b 0.0.0.0:80 app:app

