import os
from distutils.core import setup


def read_file_into_string(filename):
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


def get_readme():
    for name in ('README', 'README.rst', 'README.md'):
        if os.path.exists(name):
            return read_file_into_string(name)
    return ''


setup(
    name='kb-pkimber-net',
    packages=['project', 'project.management', 'project.management.commands', 'project.templatetags', 'web', 'web.tests', 'web.migrations', 'settings', 'dash', 'dash.tests'],
    package_data={
        'project': [
            'static/*.*',
            'static/ico/*.*',
            'static/img/*.*',
            'static/img/project/*.*',
            'templates/*.*',
            'templates/project/*.*',
        ],

        'web': [
            'static/*.*',
            'static/web/*.*',
            'static/web/css/*.*',
            'templates/*.*',
            'templates/web/*.*',
        ],

        'dash': [
            'templates/*.*',
            'templates/contact/*.*',
            'templates/dash/*.*',
        ],
    },
    version='0.1.58',
    description='my web site',
    author='Malcolm Dinsmore',
    author_email='zebyea@gmail.com',
    url='git@github.com:pkimber/pkimber_net.git',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django :: 1.8',
        'Topic :: Office/Business :: Scheduling',
    ],
    long_description=get_readme(),
)