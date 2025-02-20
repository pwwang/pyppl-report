# TOC

(Click [here][1] to go back to github repository)

Table of contents will be automatically generated by scanning the document for headings.

If you want some headings to be excluded from TOC, you just do:

The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.

```markdown
## Exluded {toc=false}
whatever
```

Following heading will be excluded:

## TOC-excluded {toc=false}

## This is a very very very very very very very very very long heading

### This is a third-level heading

# Admonitions

:::{.admon .note head=Hello}
This is a note

```markdown
:::{.admon .note head=Hello}
This is a note
:::
```
:::

:::{.admon .warn head=Warning}
This is a warning
class: .warn/.warning
:::

:::{.admon .info head=Information}
This is an info
class: .info
:::

:::{.admon .error}
This is an error

```markdown
:::{.admon .error}
This is an error
:::
```
:::

:::{.admon .example head=Example}
This is an example
class: .example
:::

:::{.admon .info head=false}
No head

`head=false`
:::

# Tables

## Tables with all data
```table
caption: File table
file: filetable.txt
```

:::{.admon .tip title=Tip}
You can insert links into the table by using `<ALT: HREF>`.
:::

:::{.admon .note}
Numbers are rounded to 3 decimals if length > 10.
:::

## Tables with subset of data and download available
```table
caption: File table
file: filetable.txt
rows: 10
download: true
```

## Tables without data file

````markdown
```table
caption: Data table
download: true
csvargs:
  delimiter: ","
---
ID,Name,Sex,Age
1,Bob,M,49
2,Alice,F,20
```
````

```table
caption: Data table
download: true
csvargs:
  delimiter: ","
---
ID,Name,Sex,Age
1,Bob,M,49
2,Alice,F,20
```

# References/Links

- Something needs ref [[1]]
  ```markdown
      - Something needs ref [[ 1 ]] <!--- No space in real case  -->

      - Another statement needs ref [[ 2 ]]

      ... ...

      [[1]]: ref1
      [[2]]: ref2
  ```
- Another statement needs ref [[2]]

- [A link with attributes](somelink "title"){a=1 b=2 c="xy" d=False f="m, n"}
  ```markdown
  [A link with attributes](somelink "title"){a=1 b=2 c="xy" d=False f="m, n"}

  ```

- [A downloadable link](./downloadfile.txt){download=true}
  ```markdown
  [A downloadable link](./downloadfile.txt){download=true}
  ```

  :::{.admon .note}
  If links are relative path to local files, they should be relative to the markdown file.
  :::

# Images

:::{.admon .note}
Images are lazy-loaded.
:::

## Add a single image

```markdown
<!-- empty line -->
![Snapshot](./snapshot.png){attributes ...}
<!-- empty line -->
```

![Snapshot](./snapshot.png)

## Add images as a combined figure

```markdown
<!-- no empty lines among the images -->
![Snapshot](./snapshot.png)
![Snapshot](./snapshot.png)
![Snapshot](./snapshot.png)
```

![Snapshot](./snapshot.png)
![Snapshot](./snapshot.png)
![Snapshot](./snapshot.png)

:::{.admon .note}
Relative image path should be relative to the markdown file.

When `pyppl_report` work as a `PyPPL` plugin, we usually pass the absolute path.
However, when it works as a CLI tool, relative path may be used.
:::

# Panels

A set of panels are blocks that only occupy one panel space in the page by using tabs or accordions,
based on the number of this set of panels.

## Auto-decision to use tabs or accordions

When number of panels <= `4` we will use tabs, otherwise accordions are used.

```markdown
::: {.panel head=Panel1}
Panel1 contents ...
:::

::: {.panel head=Panel2}
![Snapshot](./snapshot.png)
:::

```

:::{.admon .tip}

We can also use headings (`H1` up to `H5`) as the head/title of the panel, which will
be useful if you want to put the headings in TOC.
```markdown
::: {.panel}
### Panel1

Panel1 contents ...
:::

::: {.panel}
### Panel2

![Snapshot](./snapshot.png)
:::
```

:::

::: {.panel}
### Panel1

Panel1 contents ...
:::

::: {.panel}
### Panel2

![Snapshot](./snapshot.png)
:::

::: {.admon .note}
A collection of `panel`s will be automatically formed a tab or accordion sets. However, they
have to be adjacent. Otherwise, they will be built as separate sets of tabs or accordions.
:::

## Accordions

::: {.panel}
### Panel1
Panel1 contents
:::

::: {.panel head=Panel2}
Panel2 contents

This panel will be hidden in TOC, as I used:
`::: {.panel head=Panel2}`
:::

::: {.panel}
### Panel3
Panel3 contents
:::

::: {.panel}
### Panel4

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.

The quick brown fox jumps over the lazy dog.
:::

::: {.panel}
### Panel5

![Snapshot](./snapshot.png)
:::

::: {.panel}
### Panel6
:::

## Force tabs or accordions

```markdown
::: {.panel .tab head=Panel1}
panel1
:::

::: {.panel head=Panel2}
panel2
:::
```

```markdown
::: {.panel .accordion head=Panel1}
The quick brown fox jumps over the lazy dog.
:::

::: {.panel head=Panel2}
panel2
:::
```

[[1]]: ref1
[[2]]: ref2

[1]: https://github.com/pwwang/pyppl_report
