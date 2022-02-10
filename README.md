# Error explainer

Error explainer is a tool for use with Jupyter notebooks that translates Python error messages into plain English to help those learning Python.

<img src="img/error_explainer_demo.gif" alt="drawing" width="800"/>

This tool was developed as part of a research project to fulfil the requirements of the Post Graduate Certificate in Academic Practice (PGCAP) [1], as a step toward becoming a fellow of the Higher Education Academy [2].

For any suggestions or questions, contact Carl Gwilliam [carl.gwilliam (at) liverpool.ac.uk)] and/or Tessa Charles [tessa.charles (at) liverpool.ac.uk)].

## Usage

To use the error explainer download (or clone and fork) `error_explanation.py` and place it in the same directory as the Jupyter notebook.

Open the Jupyter notebook and import the module via,

```sh
import error_explainer
```

That's it! The next time you encounter an Python error, an explanation will appear directly below the error in plain English.


You can optionally log the error messages encountered by setting `logging` to `yes` in the `config.ini` file.  
This file can also be used to configure the paths and some of the messages. 

## References

[1] https://www.liverpool.ac.uk/eddev/supporting-teaching/pgcap
[2] https://www.advance-he.ac.uk/fellowship
                                   

