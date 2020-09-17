## Roadmap

## Components
<table>
<thead>
<tr><th>title            </th><th>body                                             </th><th>labels  </th></tr>
</thead>
<tbody>
<tr><td>roadmap generator</td><td>create a roadmap markdown from csv file generator</td><td>estimate</td></tr>
<tr><td>issue uploader   </td><td>create gh issue from csv file uplod script       </td><td>estimate</td></tr>
</tbody>
</table>

## Roadmap Help
The generate.py script uses entries in components.csv and the template file roadmap-template.md to automatically generate the roadmap page. If you wish to update the roadmap page, make changes to the roadmap template file in docs_dev and edit the entries in the components file using your favorite csv editor. Then run generate.py to update those changes to the official page in the docs folder.
**NOTE**: If you make changes to ROADMAP.md, they will be overwritten whenever you run generate.py
