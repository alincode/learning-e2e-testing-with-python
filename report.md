# 報表

可輸出的格式

```
behave -f help
```

```
Available formatters:
  json           JSON dump of test run
  json.pretty    JSON dump of test run (human readable)
  null           Provides formatter that does not output anything.
  plain          Very basic formatter with maximum compatibility
  pretty         Standard colourised pretty formatter
  progress       Shows dotted progress for each executed scenario.
  progress2      Shows dotted progress for each executed step.
  progress3      Shows detailed progress for each step of a scenario.
  rerun          Emits scenario file locations of failing scenarios
  sphinx.steps   Generate sphinx-based documentation for step definitions.
  steps          Shows step definitions (step implementations).
  steps.catalog  Shows non-technical documentation for step definitions.
  steps.doc      Shows documentation for step definitions.
  steps.usage    Shows how step definitions are used by steps.
  tags           Shows tags (and how often they are used).
  tags.location  Shows tags and the location where they are used.

```

## pretty 報表

```
behave -f pretty
```

![](assets/behave_f_pretty.png)

## Junit 報表

```
behave --junit
```

會產生一個 xml 檔

![](assets/junit1.png)

![](assets/junit2.png)
