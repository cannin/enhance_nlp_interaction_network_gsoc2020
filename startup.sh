if [ $# -eq 0 ]
    then
        echo "Please enter parameters YAML file path as argument"
        exit
fi

if [ ! -f $1 ]; then
    echo "Parameters file not found"
    exit
fi

echo "Step 1/2: Running Python notebooks"
papermill Reactome_Failed_Query_Analysis.ipynb failed_query_analysis.ipynb --log-output -f $1
papermill Reactome_PMID_Metadata_Extraction.ipynb pmid_metadata.ipynb --log-output -f $1

echo "Step 2/2: Running R Notebook"
cp $1 ./parameters_sample.yml
R -e "rmarkdown::render('Reactome_Analysis.Rmd',output_file='analysis_output.html')"

echo "Output file : analysis_output.nb.html"
echo "DONE"