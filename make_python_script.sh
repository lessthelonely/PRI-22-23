jupyter nbconvert --to python notebook.ipynb --stdout | grep -v -e "^get_ipython" | python
