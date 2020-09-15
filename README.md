# leetcodeSpider
leetcode网站用户信息和每日一题的爬虫
## 使用方法
### 获取用户信息
使用 getUserInfo(userSlug) 函数即可<br>
其中userSlug可从用户leetcode主页获得

## 函数说明
### imageInHtmlToText(content: str)
#### 参数说明
content：待处理的html字段

#### 返回类型
返回类型为tuple<br>
其中第一个元素为被分割的文字片段列表，其中图片的链接被以 iMaGe+编号 命名的str替换<br>
第二个元素为按顺序排列的片段中含有的图片的连接，与第一个元素中的 iMaGe+编号 按顺序对应

#### 示例
待处理数据：
```
<p>编写一个程序，通过已填充的空格来解决数独问题。</p>

<p>一个数独的解法需<strong>遵循如下规则</strong>：</p>

<ol>
	<li>数字&nbsp;<code>1-9</code>&nbsp;在每一行只能出现一次。</li>
	<li>数字&nbsp;<code>1-9</code>&nbsp;在每一列只能出现一次。</li>
	<li>数字&nbsp;<code>1-9</code>&nbsp;在每一个以粗实线分隔的&nbsp;<code>3x3</code>&nbsp;宫内只能出现一次。</li>
</ol>

<p>空白格用&nbsp;<code>&#39;.&#39;</code>&nbsp;表示。</p>

<p><img src="http://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png"></p>

<p><small>一个数独。</small></p>

<p><img src="http://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png"></p>

<p><small>答案被标成红色。</small></p>

<p><strong>Note:</strong></p>

<ul>
	<li>给定的数独序列只包含数字&nbsp;<code>1-9</code>&nbsp;和字符&nbsp;<code>&#39;.&#39;</code>&nbsp;。</li>
	<li>你可以假设给定的数独只有唯一解。</li>
	<li>给定数独永远是&nbsp;<code>9x9</code>&nbsp;形式的。</li>
</ul>
```
返回数据：
```
(
    [
        "编写一个程序，通过已填充的空格来解决数独问题。\n一个数独的解法需遵循如下规则：\n\t数字\xa01-9\xa0在每一行只能出现一次。\n\t数字\xa01-9\xa0在每一列只能出现一次。\n\t数字\xa01-9\xa0在每一个以粗实线分隔的\xa03x3\xa0宫内只能出现一次。\n空白格用\xa0'.'\xa0表示。\n", 
        'iMaGe0', 
        '\n一个数独。\n', 
        'iMaGe1', 
        "\n答案被标成红色。\nNote:\n\t给定的数独序列只包含数字\xa01-9\xa0和字符\xa0'.'\xa0。\n\t你可以假设给定的数独只有唯一解。\n\t给定数独永远是\xa09x9\xa0形式的。\n"
    ], 
    [
        'http://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png', 
        'http://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png'
    ]
)
```
