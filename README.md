# Error explainer

Error explainer is a tool for use with Jupyter notebooks that translates Python error messages into plain English to help those learning Python.

<img src="img/error_explainer_demo.gif" alt="drawing" width="800"/>

This tool was developed as part of a reserach project to fulfill the requirements of the Post Graduate Certificate in Academic Practice (PGCAP) [1], as a step toward becoming a fellow of the Higher Education Academy [2].

For any suggestions or questions, contact Carl Gwilliam [carl.gwilliam (at) liverpool.ac.uk)] and/or Tessa Charles [tessa.charles (at) liverpool.ac.uk)].

## Usage

To use the error explainer download (or clone and fork) `error_explanation.py` and place it in the same directory as the Jupyter notebook.

Open the Jupyter notebook and import the module via,

```sh
import error_explainer
```

That's it! The next time you encouter an Python error, an explaination will appear directly below the error in plain English.

The modules paths and some of the messages can be configured by editing the `config.ini` file



## References

[1] https://www.liverpool.ac.uk/eddev/supporting-teaching/pgcap
[2] https://www.advance-he.ac.uk/fellowship
                                   

