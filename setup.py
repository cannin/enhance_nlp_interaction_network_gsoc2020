import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


def main():
    install_list = [
        'indra',
        'pyjnius==1.3.0',
        'requests',
        'tqdm'
    ]
    setuptools.setup(
        name="reactome_query_utils",
        version="0.0.1",
        author="PritiShaw",
        author_email="pritishaw0103@gmail.com",
        description="This package contains support files required for running Reactome Analysis",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/cannin/enhance_nlp_interaction_network_gsoc2020",
        packages=setuptools.find_packages(),
        install_requires=install_list,
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.5',
    )


if __name__ == '__main__':
    main()
