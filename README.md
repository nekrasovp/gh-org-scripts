# gh-org-scripts

[![licence badge]][licence]
[![stars badge]][stars]
[![forks badge]][forks]
[![issues badge]][issues]

[licence badge]:https://img.shields.io/badge/license-MIT-blue.svg
[stars badge]:https://img.shields.io/github/stars/nekrasovp/gh-org-scripts.svg
[forks badge]:https://img.shields.io/github/forks/nekrasovp/gh-org-scripts.svg
[issues badge]:https://img.shields.io/github/issues/nekrasovp/gh-org-scripts.svg

[licence]:https://github.com/nekrasovp/gh-org-scripts/blob/master/LICENSE.md
[stars]:https://github.com/nekrasovp/gh-org-scripts/stargazers
[forks]:https://github.com/nekrasovp/gh-org-scripts/network
[issues]:https://github.com/nekrasovp/gh-org-scripts/issues

Useful scripts for new GitHub project.

Navigation

- [gh-org-scripts](#gh-org-scripts)
  - [Components](#components)
  - [Roadmap](#roadmap)
  - [Github issues](#github-issues)
  - [GitHub and Git Resources](#github-and-git-resources)
  - [Markdown Wiki](#markdown-wiki)
  - [License](#license)

## Components

Example components.csv

```csv
title,body,assignee, milestone, labels
smtp key,create a password key for email client smtp forwarding, ,1,estimate
sending domain,retrieve spf and dkim records from smtp host, ,1,estimate
DNS update,add spf and dkim records from smtp host to DNS record, ,2,estimate
Send-from alias,register smtp host login details with email client, ,2,estimate
```

**[⬆ back to top](#gh-org-scripts)**

## Roadmap

The generate.py script uses entries in components.csv and the template file roadmap-template.md to automatically generate the roadmap page. If you wish to update the roadmap page, make changes to the roadmap template file and edit the entries in the components file using your favorite csv editor. Then run generate.py to update those changes.
**NOTE**: If you make changes to ROADMAP.md, they will be overwritten whenever you run generate.py

**[⬆ back to top](#gh-org-scripts)**

## Github issues

The issueuploader.py script uses entries in components.csv to automatically upload issues to github repository.
**NOTE**: Running script twice will duplicate issues

[https://developer.github.com/v3/issues/#create-an-issue](https://developer.github.com/v3/issues/#create-an-issue)

|Name|Type|Description
|---|---|---
|title|string|Required. The title of the issue.
|body|string|The contents of the issue.
|assignee|string|Login for the user that this issue should be assigned to. NOTE: Only users with push access can set the assignee for new issues. The assignee is silently dropped otherwise. This field is deprecated.
|milestone|integer|The number of the milestone to associate this issue with. NOTE: Only users with push access can set the milestone for new issues. The milestone is silently dropped otherwise.
|labels|array of strings|Labels to associate with this issue. NOTE: Only users with push access can set labels for new issues. Labels are silently dropped otherwise.
|assignees|array of strings|Logins for Users to assign to this issue. NOTE: Only users with push access can set assignees for new issues. Assignees are silently dropped otherwise.

Example

```json
{
  "title": "Found a bug",
  "body": "I'm having a problem with this.",
  "assignees": [
    "octocat"
  ],
  "milestone": 1,
  "labels": [
    "bug"
  ]
}
```

**[⬆ back to top](#gh-org-scripts)**

## GitHub and Git Resources

- [Project management, made simple] (https://github.com/features/project-management/)
- [Mastering Issues](https://guides.github.com/features/issues/)
- [Awesome GitHub Issues & PRs Templates](https://github.com/devspace/awesome-github-templates)
- [A collection of GitHub issue and pull request templates](https://github.com/stevemao/github-issue-templates)
- [About issue and pull request templates](https://docs.github.com/en/github/building-a-strong-community/about-issue-and-pull-request-templates)
- [GitHub Resources for Beginners](https://dzone.com/articles/github-resources-for-beginners)
- [Cheat-sheet](https://github.com/tiimgreen/github-cheat-sheet)
- [Awesome Github](https://github.com/Kikobeats/awesome-github)
- [Github Cheat Sheet Хабрахабр](https://habrahabr.ru/post/219219/)
- [Git and GitHub Secrets (Zach Holman)](http://confreaks.tv/videos/aloharuby2012-git-and-github-secrets)
- [More Git and GitHub Secrets (Zach Holman)](https://vimeo.com/72955426)
- [GitHub Help](https://help.github.com/)
- [Эффективное использование Github](https://habrahabr.ru/company/2gis/blog/306166/)
- [Try GIT in Browser](https://try.github.io/)
- [Bash: Основы командной строки](https://ru.hexlet.io/courses/bash/)
- [Github Guides](https://guides.github.com)
- [GitHub Flavored Markdown Spec](https://github.github.com/gfm/)
- [GitHub About issue and pull request templates](https://help.github.com/articles/about-issue-and-pull-request-templates/)
- [Pro Git book](https://git-scm.com/book/en/v2)
- [Git Command Explorer - Find the right commands you need without digging through the web](https://gitexplorer.com/)
- [git-history - Quickly browse the history of a file from any git repository](https://github.com/pomber/git-history)
- [How to teach Git](https://rachelcarmena.github.io/2018/12/12/how-to-teach-git.html)

**[⬆ back to top](#gh-org-scripts)**

## Markdown Wiki

- [Markdown - Basic writing and formatting syntax](https://help.github.com/articles/basic-writing-and-formatting-syntax/)
- [Mastering markdown](https://guides.github.com/features/mastering-markdown/)
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

**[⬆ back to top](#gh-org-scripts)**

## License

[MIT](/LICENSE)

**[⬆ back to top](#gh-org-scripts)**