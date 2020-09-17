# gh-org-scripts
Github project helpres

### Github issue parameters

https://developer.github.com/v3/issues/#create-an-issue

|Name |	Type |	Description 
|---|---|---
|title	|string|	Required. The title of the issue.
|body|	string|	The contents of the issue.
|assignee	|string	|Login for the user that this issue should be assigned to. NOTE: Only users with push access can set the assignee for new issues. The assignee is silently dropped otherwise. This field is deprecated.
|milestone	|integer	|The number of the milestone to associate this issue with. NOTE: Only users with push access can set the milestone for new issues. The milestone is silently dropped otherwise.
|labels|array of strings|	Labels to associate with this issue. NOTE: Only users with push access can set labels for new issues. Labels are silently dropped otherwise.
|assignees|	array of strings|	Logins for Users to assign to this issue. NOTE: Only users with push access can set assignees for new issues. Assignees are silently dropped otherwise.

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

Example components.csv

```csv
title,body,assignee, milestone, labels
smtp key,create a password key for email client smtp forwarding, ,1,estimate
sending domain,retrieve spf and dkim records from smtp host, ,1,estimate
DNS update,add spf and dkim records from smtp host to DNS record, ,2,estimate
Send-from alias,register smtp host login details with email client, ,2,estimate
```
