# PyCy

This repository represents a standard architecture for proejcts that are based on `Tornado` and are emplying `Cython`'s powerful functionalities to create async web services with a modular backend.

The main problem that we are addressing and providing a solution for, is being able to load a module, once, as a singleton and then use that module as some kind of source of knowledge. There are many ML/AI scripts (software, different kinds of computer programs) that work in this specific manner.

Let's say you are creating a webservice that will check existence of an specific element in a very large set of different elements. Take a [Bloom Filter](https://en.wikipedia.org/wiki/Bloom_filter) for instance. This web service can be the microservice for checking availablity of an email address or username in a bigger microservice eco-system.

In this case, there needs to be a Bloom Filter data structure, loaded somewhere in `RAM` and a service to send requests to that data structure, asking if the `user input` already exists in the data structure or not.

If you face a similar situation, you will notice that using something like `django` for this purpose, is simply not possible. We need to be able to handle large amounts of requests per second and we don't want to have multiple instances of this web service (like we do when using `gunicorn` workers to run multiple instances of a django application).

We are using this project structure to power 4 different microservices that have the same characteristics mentioned above. We needed a webservice that is processing user inputs using a Maching Learning model and responds with the answers returned from the model.

---

Services based on `pycy-engine` in torob:
* SpellChecker
* Autocomplete
* Product Category Classifier
* Query Category Classifier

---

## Files/Folder Structure

```bash
├── project
│   ├── app
│   │   ├── context.py
│   │   ├── handlers.py
│   │   ├── __init__.py
│   │   ├── mod_wrappers.py
│   │   ├── server.py
│   │   ├── urls.py
│   │   └── wall.py
│   ├── mods
│   │   ├── build.sh
│   │   ├── clean.sh
│   │   └── mod-sample
│   │       ├── sample.h
│   │       ├── sample.pyx
│   │       └── setup.py
│   ├── pycy
│   │   ├── core.py
│   │   ├── __init__.py
│   │   ├── proxy.py
│   │   └── utils.py
│   ├── logs
│   ├── run_app.py
│   └── run_proxy.py
├── supervisor.d
│   ├── proxy.ini
│   └── tornado.ini
├── README.md
├── requirements.txt
├── config.yaml
├── Dockerfile
└── supervisord.conf
```

### project

> After cloning this repository, you should rename this folder to the name of your own project.

This is the main folder that you will put your codes in. To be specific, your project's main directory, will be `project/app`. 