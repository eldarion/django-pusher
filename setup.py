from distutils.core import setup


VERSION = __import__("django_pusher").__version__


setup(
    name="django-pusher",
    version=VERSION,
    author="Eldarion",
    author_email="development@eldarion.com",
    description="an extensible profile app designed to replace the profiles apps in Pinax",
    long_description=open("README.rst").read(),
    license="BSD",
    url="http://github.com/eldarion/django-pusher/",
    packages=[
        "django_pusher",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
