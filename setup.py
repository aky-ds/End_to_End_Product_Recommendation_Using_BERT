from setuptools import setup, find_packages

def get_requirements():
    with open('requirements.txt') as f:
        requires = f.readlines()
        requires = [req.strip() for req in requires]  # Use strip() to remove newlines and spaces
        if '-e .' in requires:
            requires.remove('-e .')
    return requires

setup(
    name='End to End Product Recommendation using BERT',
    version='0.1.0',
    packages=find_packages(),
    author='ayazulhaqyousafzai',
    author_email='www.ayazkhan.com.21@gmail.com',
    description='An End to End E-commerce Product Recommendation Application which provides recommendations of products based on similarity',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=get_requirements(),  # Call the function without arguments
    python_requires='>=3.7',
)
