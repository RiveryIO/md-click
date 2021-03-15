
# dumps

# Click-md
Create md files per each command, in format of `parent-command`, under the `--docsPath` directory.

## Usage

```
Usage: mdclick dumps [OPTIONS]
```

## Options
* `basemodule` (REQUIRED): 
  * Type: STRING 
  * Default: `none`
  * Usage: `--baseModule`

  The base command module path to import


* `basecommand` (REQUIRED): 
  * Type: STRING 
  * Default: `none`
  * Usage: `--baseCommand`

  The base command function to import


* `docspath` (REQUIRED): 
  * Type: STRING 
  * Default: `none`
  * Usage: `--docsPath`

  The docs dir path to write the md files


* `help`: 
  * Type: BOOL 
  * Default: `false`
  * Usage: `--help`

  Show this message and exit.



## CLI Help

```
Usage: mdclick dumps [OPTIONS]

  # Click-md Create md files per each command, in format of `parent-command`,
  under the `--docsPath` directory.

Options:
  --baseModule TEXT   The base command module path to import  [required]
  --baseCommand TEXT  The base command function to import  [required]
  --docsPath TEXT     The docs dir path to write the md files  [required]
  --help              Show this message and exit.
```

