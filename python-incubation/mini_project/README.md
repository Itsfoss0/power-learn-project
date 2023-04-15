![plp-logo](../../logo.webp)

## Mini project
This mini project is a python script that looks for the definition of a word from a dictionary provided in in the dataset

## Usage
It's pretty much straight forwad to use

```
./word_definition.py <word> <data_set>
```

In our case, we have `data.json` provided as a data set. To search for the definition of the word `father` from the `data.json` data set, we'd

```
┌─[itsfoss@itsfoss]─[~/Desktop/PLP/python-incubation/mini_project]
└──╼ $./word_definition.py  father data.json
'father' can mean A male parent.
'feather' can mean A branching, hair-like structure that grows on the skin of birds and protects them against coldness and water and allows their wings to create lift.
┌─[itsfoss@itsfoss]─[~/Desktop/PLP/python-incubation/mini_project]
└──╼ $
```
