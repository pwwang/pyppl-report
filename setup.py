# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='pyppl_report',
    version='0.6.2',
    description='A report generating system for PyPPL',
    python_requires='==3.*,>=3.6.0',
    project_urls={
        "homepage": "https://github.com/pwwang/pyppl_report",
        "repository": "https://github.com/pwwang/pyppl_report"
    },
    author='pwwang',
    author_email='pwwang@pwwang.com',
    license='MIT',
    entry_points={"pyppl": ["pyppl_report = pyppl_report"]},
    packages=['pyppl_report', 'pyppl_report.filters'],
    package_dir={"": "."},
    package_data={
        "pyppl_report": [
            "*.bak", "templates/bootstrap/*.html",
            "templates/bootstrap/static/*.css",
            "templates/bootstrap/static/*.js", "templates/layui/*.html",
            "templates/layui/static/*.css", "templates/layui/static/*.jpg",
            "templates/layui/static/*.js", "templates/layui/static/css/*.css",
            "templates/layui/static/css/modules/*.css",
            "templates/layui/static/css/modules/laydate/default/*.css",
            "templates/layui/static/css/modules/layer/default/*.css",
            "templates/layui/static/css/modules/layer/default/*.gif",
            "templates/layui/static/css/modules/layer/default/*.png",
            "templates/layui/static/font/*.eot",
            "templates/layui/static/font/*.svg",
            "templates/layui/static/font/*.ttf",
            "templates/layui/static/font/*.woff",
            "templates/layui/static/font/*.woff2",
            "templates/layui/static/images/face/*.gif",
            "templates/layui/static/lay/*.js",
            "templates/layui/static/lay/modules/*.js",
            "templates/layui/static/lay/modules/mobile/*.js",
            "templates/semantic/*.html", "templates/semantic/static/*.css",
            "templates/semantic/static/*.js",
            "templates/semantic/static/themes/default/assets/fonts/*.eot",
            "templates/semantic/static/themes/default/assets/fonts/*.svg",
            "templates/semantic/static/themes/default/assets/fonts/*.ttf",
            "templates/semantic/static/themes/default/assets/fonts/*.woff",
            "templates/semantic/static/themes/default/assets/fonts/*.woff2",
            "templates/semantic/static/themes/default/assets/images/*.png"
        ]
    },
    install_requires=[
        'cmdy', 'liquidpy', 'panflute==1.11.*', 'pyppl', 'toml==0.*,>=0.10.0'
    ],
    extras_require={"dev": ["pyparam", "pytest", "pytest-cov"]},
)
