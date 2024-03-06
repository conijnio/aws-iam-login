# CHANGELOG



## v0.3.4 (2024-03-06)

### Chore

* chore(deps): Bump boto3 from 1.34.50 to 1.34.55 (#172)

Bumps [boto3](https://github.com/boto/boto3) from 1.34.50 to 1.34.55.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.34.55&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;cloudformation&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add
DetailedStatus field to DescribeStackEvents and DescribeStacks APIs&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;fsx&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added support
for creating FSx for NetApp ONTAP file systems with up to 12 HA pairs,
delivering up to 72 GB/s of read throughput and 12 GB/s of write
throughput.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;organizations&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Documentation update for AWS Organizations&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.54&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;accessanalyzer&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Fixed a typo in description field.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;autoscaling&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] With
this release, Amazon EC2 Auto Scaling groups, EC2 Fleet, and Spot Fleet
improve the default price protection behavior of attribute-based
instance type selection of Spot Instances, to consistently select from a
wide range of instance types.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ec2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] With this
release, Amazon EC2 Auto Scaling groups, EC2 Fleet, and Spot Fleet
improve the default price protection behavior of attribute-based
instance type selection of Spot Instances, to consistently select from a
wide range of instance types.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.53&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;docdb-elastic&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Launched Elastic Clusters Readable Secondaries, Start/Stop, Configurable
Shard Instance count, Automatic Backups and Snapshot Copying&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;eks&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added support
for new AL2023 AMIs to the supported AMITypes.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;lexv2-models&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release makes AMAZON.QnAIntent generally available in Amazon Lex. This
generative AI feature leverages large language models available through
Amazon Bedrock to automate frequently asked questions (FAQ) experience
for end-users.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;migrationhuborchestrator&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] Adds new CreateTemplate, UpdateTemplate and
DeleteTemplate APIs.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;quicksight&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
TooltipTarget for Combo chart visuals; ColumnConfiguration limit
increase to 2000; Documentation Update&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;sagemaker&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adds
support for ModelDataSource in Model Packages to support unzipped
models. Adds support to specify SourceUri for models which allows
registration of models without mandating a container for hosting. Using
SourceUri, customers can decouple the model from hosting information
during registration.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;securitylake&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add
capability to update the Data Lake&#39;s MetaStoreManager Role in order to
perform required data lake updates to use Iceberg table format in their
data lake or update the role for any other reason.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.52&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;batch&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds Batch support for configuration of multicontainer jobs in ECS,
Fargate, and EKS. This support is available for all types of jobs,
including both array jobs and multi-node parallel jobs.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;bedrock-agent-runtime&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] This release adds support to override search
strategy performed by the Retrieve and RetrieveAndGenerate APIs for
Amazon Bedrock Agents&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ce&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
introduces the new API &#39;GetApproximateUsageRecords&#39;, which retrieves
estimated usage records for hourly granularity or resource-level data at
daily granularity.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ec2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
increases the range of MaxResults for
GetNetworkInsightsAccessScopeAnalysisFindings to 1,000.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;iot&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
reduces the maximum results returned per query invocation from 500 to
100 for the SearchIndex API. This change has no implications as long as
the API is invoked until the nextToken is NULL.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;wafv2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] AWS WAF now
supports configurable time windows for request aggregation with
rate-based rules. Customers can now select time windows of 1 minute, 2
minutes or 10 minutes, in addition to the previously supported 5
minutes.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.51&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;amplifyuibuilder&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] We
have added the ability to tag resources after they are created&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/93451cd44bdd0bc070fa4d078b5392db0f4400dd&#34;&gt;&lt;code&gt;93451cd&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.55&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/06be6452cbd155998da1a84399bd18519bb9256b&#34;&gt;&lt;code&gt;06be645&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.55&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/44f84c7287518f9ff12a573d7e9d078ac4c4b858&#34;&gt;&lt;code&gt;44f84c7&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/40038ca4e271663fa483fe57302f7f83310c6719&#34;&gt;&lt;code&gt;40038ca&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.54&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/d2faa68d4bf2e55939f9221dcb0eadaafdc2d48f&#34;&gt;&lt;code&gt;d2faa68&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.54&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/21239193bff10fb248a56fd1e7b020c78d59cd14&#34;&gt;&lt;code&gt;2123919&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.54&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/e2a39f9e434ce6a10cdddab3825436890d9e81ce&#34;&gt;&lt;code&gt;e2a39f9&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/914c71b63c04c295aa06b6f62af9b4de8ec87de7&#34;&gt;&lt;code&gt;914c71b&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.53&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/b1db713392afe58c390499d4bf1d1004ae68c547&#34;&gt;&lt;code&gt;b1db713&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.53&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/0fdef8bab917e9fcdc2269816be535a660a6ad01&#34;&gt;&lt;code&gt;0fdef8b&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.53&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.34.50...1.34.55&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.34.50&amp;new-version=1.34.55)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`6d2ffb7`](https://github.com/conijnio/aws-iam-login/commit/6d2ffb76ba605cd15ba04f71b4d1a97fd9eff016))

* chore(deps-dev): Bump pytest from 8.0.1 to 8.0.2 (#171)

Bumps [pytest](https://github.com/pytest-dev/pytest) from 8.0.1 to
8.0.2.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pytest-dev/pytest/releases&#34;&gt;pytest&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;8.0.2&lt;/h2&gt;
&lt;h1&gt;pytest 8.0.2 (2024-02-24)&lt;/h1&gt;
&lt;h2&gt;Bug Fixes&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11895&#34;&gt;#11895&lt;/a&gt;:
Fix collection on Windows where initial paths contain the short version
of a path (for example &lt;code&gt;c:\PROGRA~1\tests&lt;/code&gt;).&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11953&#34;&gt;#11953&lt;/a&gt;:
Fix an &lt;code&gt;IndexError&lt;/code&gt; crash raising from
&lt;code&gt;getstatementrange_ast&lt;/code&gt;.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/12021&#34;&gt;#12021&lt;/a&gt;:
Reverted a fix to [--maxfail]{.title-ref} handling in pytest 8.0.0
because it caused a regression in pytest-xdist whereby session fixture
teardowns may get executed multiple times when the max-fails is
reached.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/31afeeb0df0e8bdab1325b5992a2cc733e981e82&#34;&gt;&lt;code&gt;31afeeb&lt;/code&gt;&lt;/a&gt;
Prepare release version 8.0.2&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/1b00a2f4fba7859c31dab4f5afdd9e1f07cbdd1e&#34;&gt;&lt;code&gt;1b00a2f&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/12025&#34;&gt;#12025&lt;/a&gt;
from pytest-dev/backport-12022-to-8.0.x&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/ff2f66d84affb0fbcbf841b1897c7599026730bc&#34;&gt;&lt;code&gt;ff2f66d&lt;/code&gt;&lt;/a&gt;
[8.0.x] Revert &amp;quot;Fix teardown error reporting when
&lt;code&gt;--maxfail=1&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11721&#34;&gt;#11721&lt;/a&gt;)&amp;quot;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/8a8eed609c3c20da452446e1686df41ebda96d11&#34;&gt;&lt;code&gt;8a8eed6&lt;/code&gt;&lt;/a&gt;
[8.0.x] Fix collection of short paths on Windows (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/12024&#34;&gt;#12024&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/74346f027c205e5daffe66801094293744e8d85f&#34;&gt;&lt;code&gt;74346f0&lt;/code&gt;&lt;/a&gt;
[8.0.x] Allow Sphinx 7.x (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/12005&#34;&gt;#12005&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/b7657b4d6b69ee26e00d9a71c4d208506f644462&#34;&gt;&lt;code&gt;b7657b4&lt;/code&gt;&lt;/a&gt;
[8.0.x] Disallow Sphinx 6 and 7 (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/12001&#34;&gt;#12001&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/feb7c5e12ee3374b2c7c773614d76811ad21a4f4&#34;&gt;&lt;code&gt;feb7c5e&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11999&#34;&gt;#11999&lt;/a&gt;
from pytest-dev/backport-11996-to-8.0.x&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/090965574ece50c6be955719ced2a9cf8daaee17&#34;&gt;&lt;code&gt;0909655&lt;/code&gt;&lt;/a&gt;
[8.0.x] code: fix &lt;code&gt;IndexError&lt;/code&gt; crash in
&lt;code&gt;getstatementrange_ast&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/68524d48586e7f8d070fc1146e5ff90e770d0382&#34;&gt;&lt;code&gt;68524d4&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11993&#34;&gt;#11993&lt;/a&gt;
from pytest-dev/release-8.0.1&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/pytest-dev/pytest/compare/8.0.1...8.0.2&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=pytest&amp;package-manager=pip&amp;previous-version=8.0.1&amp;new-version=8.0.2)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`e70b2ff`](https://github.com/conijnio/aws-iam-login/commit/e70b2ffb033d692180396d41a8fd18a5a23aec25))

* chore(deps): Bump boto3 from 1.34.45 to 1.34.50 (#170)

Bumps [boto3](https://github.com/boto/boto3) from 1.34.45 to 1.34.50.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.34.50&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;apigateway&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Documentation updates for Amazon API Gateway.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;drs&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added volume
status to DescribeSourceServer replicated volumes.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;kafkaconnect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adds
support for tagging, with new TagResource, UntagResource and
ListTagsForResource APIs to manage tags and updates to existing APIs to
allow tag on create. This release also adds support for the new
DeleteWorkerConfiguration API.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;rds&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds support for gp3 data volumes for Multi-AZ DB Clusters.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.49&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;appsync&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Documentation only updates for AppSync&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;qldb&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Clarify
possible values for KmsKeyArn and EncryptionDescription.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;rds&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add pattern and
length based validations for DBShardGroupIdentifier&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;rum&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Doc-only update
for new RUM metrics that were added&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.48&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;internetmonitor&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
This release adds IPv4 prefixes to health events&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;kinesisvideo&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Increasing NextToken parameter length restriction for List APIs from 512
to 1024.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.47&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;iotevents&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Increase
the maximum length of descriptions for Inputs, Detector Models, and
Alarm Models&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;lookoutequipment&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
This release adds a field exposing model quality to read APIs for
models. It also adds a model quality field to the API response when
creating an inference scheduler.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;medialive&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] MediaLive
now supports the ability to restart pipelines in a running channel.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ssm&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds support for sharing Systems Manager parameters with other AWS
accounts.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.46&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;dynamodb&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Publishing
quick fix for doc only update.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;firehose&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release updates a few Firehose related APIs.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;lambda&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add .NET 8
(dotnet8) Runtime support to AWS Lambda.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/48accbeba1e16e9e626fd9c4de98a0792a36d671&#34;&gt;&lt;code&gt;48accbe&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.50&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/22a5587a274a02516ba33457fec7bc8c66429dc1&#34;&gt;&lt;code&gt;22a5587&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.50&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/325efa9f75275fe3f7634a56880c66ab3cbd31d5&#34;&gt;&lt;code&gt;325efa9&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/c6818e2e61af105b34f00a79844b6f9df8de808e&#34;&gt;&lt;code&gt;c6818e2&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.49&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/b3c158c62aa2a1314dc0ec78caea1ea976abd1a0&#34;&gt;&lt;code&gt;b3c158c&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.49&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/d887ea8016e43152d0a17d550dc1b43627ebd796&#34;&gt;&lt;code&gt;d887ea8&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.49&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/eab896ef2d1cf3d16116e65007f60be51fe79df0&#34;&gt;&lt;code&gt;eab896e&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/bf6204a7b098578648010aba17c0138eb1740603&#34;&gt;&lt;code&gt;bf6204a&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.48&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/0bb57def7d747f5dfbe5e4ea4f25689e98f1b648&#34;&gt;&lt;code&gt;0bb57de&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.48&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/3200e73ea6e6812cd341a36207f662abd4e7a00f&#34;&gt;&lt;code&gt;3200e73&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.48&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.34.45...1.34.50&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.34.45&amp;new-version=1.34.50)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`e5b37b4`](https://github.com/conijnio/aws-iam-login/commit/e5b37b41f6ee29258ea7397f5a7f32c5cf533b55))

* chore(deps-dev): Bump cryptography from 42.0.2 to 42.0.4 (#169)

Bumps [cryptography](https://github.com/pyca/cryptography) from 42.0.2
to 42.0.4.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst&#34;&gt;cryptography&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;p&gt;42.0.4 - 2024-02-20&lt;/p&gt;
&lt;pre&gt;&lt;code&gt;
* Fixed a null-pointer-dereference and segfault that could occur when
creating
a PKCS#12 bundle. Credit to **Alexander-Programming** for reporting the
  issue. **CVE-2024-26130**
* Fixed ASN.1 encoding for PKCS7/SMIME signed messages. The fields
``SMIMECapabilities``
and ``SignatureAlgorithmIdentifier`` should now be correctly encoded
according to the
  definitions in :rfc:`2633` :rfc:`3370`.
&lt;p&gt;.. _v42-0-3:&lt;/p&gt;
&lt;p&gt;42.0.3 - 2024-02-15
&lt;/code&gt;&lt;/pre&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Fixed an initialization issue that caused key loading failures for
some
users.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;.. _v42-0-2:&lt;/p&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/fe18470f7d05f963e7267e34fdf985d81ea6ceea&#34;&gt;&lt;code&gt;fe18470&lt;/code&gt;&lt;/a&gt;
Bump for 42.0.4 release (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10445&#34;&gt;#10445&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/aaa2dd06ed470695de818405a982d4c459869803&#34;&gt;&lt;code&gt;aaa2dd0&lt;/code&gt;&lt;/a&gt;
Fix ASN.1 issues in PKCS#7 and S/MIME signing (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10373&#34;&gt;#10373&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10442&#34;&gt;#10442&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/7a4d012991061974da5d9cb7614de65eac94f49b&#34;&gt;&lt;code&gt;7a4d012&lt;/code&gt;&lt;/a&gt;
Fixes &lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10422&#34;&gt;#10422&lt;/a&gt;
-- don&#39;t crash when a PKCS#12 key and cert don&#39;t match (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10423&#34;&gt;#10423&lt;/a&gt;)
...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/df314bb182bdfd661333969a94325e4680d785f6&#34;&gt;&lt;code&gt;df314bb&lt;/code&gt;&lt;/a&gt;
backport actions m1 switch to 42.0.x (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10415&#34;&gt;#10415&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/c49a7a5271178c6e8ef36fa1c499f62c63ec19b9&#34;&gt;&lt;code&gt;c49a7a5&lt;/code&gt;&lt;/a&gt;
changelog and version bump for 42.0.3 (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10396&#34;&gt;#10396&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/396bcf64c5be826ec00e7d7f45838c858c049cbc&#34;&gt;&lt;code&gt;396bcf6&lt;/code&gt;&lt;/a&gt;
fix provider loading take two (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10390&#34;&gt;#10390&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10395&#34;&gt;#10395&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/0e0e46f5f73f477b8ee9682738c42129d5d60177&#34;&gt;&lt;code&gt;0e0e46f&lt;/code&gt;&lt;/a&gt;
backport: initialize openssl&#39;s legacy provider in rust (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10323&#34;&gt;#10323&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10333&#34;&gt;#10333&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/pyca/cryptography/compare/42.0.2...42.0.4&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cryptography&amp;package-manager=pip&amp;previous-version=42.0.2&amp;new-version=42.0.4)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)
You can disable automated security fix PRs for this repo from the
[Security Alerts
page](https://github.com/Nr18/aws-iam-login/network/alerts).

&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`bd93716`](https://github.com/conijnio/aws-iam-login/commit/bd9371676483b3c1831ce19b9276c4623866e04f))

* chore(deps): Bump boto3 from 1.34.40 to 1.34.45 (#168)

Bumps [boto3](https://github.com/boto/boto3) from 1.34.40 to 1.34.45.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.34.45&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;amplify&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release contains API changes that enable users to configure their
Amplify domains with their own custom SSL/TLS certificate.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;chatbot&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds support for AWS Chatbot. You can now monitor, operate, and
troubleshoot your AWS resources with interactive ChatOps using the AWS
SDK.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;config&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Documentation updates for the AWS Config CLI&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ivs&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Changed
description for latencyMode in Create/UpdateChannel and
Channel/ChannelSummary.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;keyspaces&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Documentation updates for Amazon Keyspaces&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;mediatailor&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
MediaTailor: marking #AdBreak.OffsetMillis as required.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.44&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;connectparticipant&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Doc only update to GetTranscript API reference guide to inform users
about presence of events in the chat transcript.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;emr&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] adds fine
grained control over Unhealthy Node Replacement to Amazon
ElasticMapReduce&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;firehose&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds support for Data Message Extraction for decompressed
CloudWatch logs, and to use a custom file extension or time zone for S3
destinations.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;lambda&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Documentation-only updates for Lambda to clarify a number of existing
actions and properties.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;rds&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Doc only update
for a valid option in DB parameter group&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;sns&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
marks phone numbers as sensitive inputs.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.43&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;artifact&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This is
the initial SDK release for AWS Artifact. AWS Artifact provides
on-demand access to compliance and third-party compliance reports. This
release includes access to List and Get reports, along with their
metadata. This release also includes access to AWS Artifact
notifications settings.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;codepipeline&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add
ability to override timeout on action level.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;detective&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Doc only
updates for content enhancement&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;guardduty&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Marked
fields IpAddressV4, PrivateIpAddress, Email as Sensitive.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;healthlake&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds a new response parameter, JobProgressReport, to the
DescribeFHIRImportJob and ListFHIRImportJobs API operation.
JobProgressReport provides details on the progress of the import job on
the server.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;opensearch&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adds
additional supported instance types.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;polly&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Amazon Polly
adds 1 new voice - Burcu (tr-TR)&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;sagemaker&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds a new API UpdateClusterSoftware for SageMaker HyperPod.
This API allows users to patch HyperPod clusters with latest platform
softwares.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;secretsmanager&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Doc
only update for Secrets Manager&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;endpoint-rules&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update endpoint-rules client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.42&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;controltower&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adds
support for new Baseline and EnabledBaseline APIs for automating
multi-account governance.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;lookoutequipment&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
This feature allows customers to see pointwise model diagnostics results
for their models.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;qbusiness&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds the metadata-boosting feature, which allows customers to
easily fine-tune the underlying ranking of retrieved RAG passages in
order to optimize Q&amp;amp;A answer relevance. It also adds new feedback
reasons for the PutFeedback API.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.41&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;bugfix:ContainerProvider: [&lt;code&gt;botocore&lt;/code&gt;] Properly refreshes
token from file from EKS in ContainerProvider&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;lightsail&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds support to upgrade the major version of a database.&lt;/li&gt;
&lt;/ul&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/f08cf384a62f0e2d6378bb700dcd57476d64eccb&#34;&gt;&lt;code&gt;f08cf38&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.45&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/4d07d238eecce0443e4f78cde9d8e12fefd740af&#34;&gt;&lt;code&gt;4d07d23&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.45&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/41532a77467d7704a0095831915c2626bf65a5bc&#34;&gt;&lt;code&gt;41532a7&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/3954a1a73df346ea0361d4bc52e17b7a710b2c27&#34;&gt;&lt;code&gt;3954a1a&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.44&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/90dc6e8af3a37fff3a00e769c0989e051a56e20d&#34;&gt;&lt;code&gt;90dc6e8&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.44&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/ae78e0a42969065623e5c16e6ca917dca57e4dae&#34;&gt;&lt;code&gt;ae78e0a&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.44&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/894c06217a1c7800fd057a67aa62846856f9f6df&#34;&gt;&lt;code&gt;894c062&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/1ff34a81a9557e501c593c3f87c0cb555d5c93bf&#34;&gt;&lt;code&gt;1ff34a8&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.43&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/b320cd66609aa078be5271fdf99a052e78b14203&#34;&gt;&lt;code&gt;b320cd6&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.43&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/26e6124f1de174b6931b34ed9ae4d6a8a83b4021&#34;&gt;&lt;code&gt;26e6124&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.43&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.34.40...1.34.45&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.34.40&amp;new-version=1.34.45)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`2b49a1b`](https://github.com/conijnio/aws-iam-login/commit/2b49a1b792c309bb6d7b5d466cb7f3eb510326d0))

* chore(deps-dev): Bump pytest from 8.0.0 to 8.0.1 (#167)

Bumps [pytest](https://github.com/pytest-dev/pytest) from 8.0.0 to
8.0.1.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pytest-dev/pytest/releases&#34;&gt;pytest&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;8.0.1&lt;/h2&gt;
&lt;h1&gt;pytest 8.0.1 (2024-02-16)&lt;/h1&gt;
&lt;h2&gt;Bug Fixes&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11875&#34;&gt;#11875&lt;/a&gt;:
Correctly handle errors from
&lt;code&gt;getpass.getuser&lt;/code&gt;{.interpreted-text role=&amp;quot;func&amp;quot;} in
Python 3.13.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11879&#34;&gt;#11879&lt;/a&gt;:
Fix an edge case where &lt;code&gt;ExceptionInfo._stringify_exception&lt;/code&gt;
could crash &lt;code&gt;pytest.raises&lt;/code&gt;{.interpreted-text
role=&amp;quot;func&amp;quot;}.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11906&#34;&gt;#11906&lt;/a&gt;:
Fix regression with &lt;code&gt;pytest.warns&lt;/code&gt;{.interpreted-text
role=&amp;quot;func&amp;quot;} using custom warning subclasses which have more
than one parameter in their [__init__]{.title-ref}.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11907&#34;&gt;#11907&lt;/a&gt;:
Fix a regression in pytest 8.0.0 whereby calling
&lt;code&gt;pytest.skip&lt;/code&gt;{.interpreted-text role=&amp;quot;func&amp;quot;} and
similar control-flow exceptions within a
&lt;code&gt;pytest.warns()&lt;/code&gt;{.interpreted-text role=&amp;quot;func&amp;quot;}
block would get suppressed instead of propagating.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11929&#34;&gt;#11929&lt;/a&gt;:
Fix a regression in pytest 8.0.0 whereby autouse fixtures defined in a
module get ignored by the doctests in the module.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11937&#34;&gt;#11937&lt;/a&gt;:
Fix a regression in pytest 8.0.0 whereby items would be collected in
reverse order in some circumstances.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/d7d320a15a1f8dae909e0aa71f20ab5daeaa42d3&#34;&gt;&lt;code&gt;d7d320a&lt;/code&gt;&lt;/a&gt;
Prepare release version 8.0.1&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/93699166dc3d90676b126d2b1615fbd41cf0be4d&#34;&gt;&lt;code&gt;9369916&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11992&#34;&gt;#11992&lt;/a&gt;
from bluetech/backport-11991&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/a232abd56cd7ddc0d6dbeefd851c538ec547ab06&#34;&gt;&lt;code&gt;a232abd&lt;/code&gt;&lt;/a&gt;
[8.0.x] recwarn: fix pytest.warns handling of Warnings with multiple
arguments&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/92203d2b78135446510ec70d46452937effcb1d9&#34;&gt;&lt;code&gt;92203d2&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11990&#34;&gt;#11990&lt;/a&gt;
from bluetech/backport-11920&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/f1aa9226ac5b1962fdad442652765d5e589c7137&#34;&gt;&lt;code&gt;f1aa922&lt;/code&gt;&lt;/a&gt;
[8.0.x] recwarn: let base exceptions propagate through
&lt;code&gt;pytest.warns&lt;/code&gt; again&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/d86d08156337b40ad0cf6e4bfe38ecfa0e5eb5bd&#34;&gt;&lt;code&gt;d86d081&lt;/code&gt;&lt;/a&gt;
[8.0.x] Added &lt;code&gt;logot&lt;/code&gt; to the plugin list (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11977&#34;&gt;#11977&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/c554c3d200747f9f56b4054619ba4fb6f8910bb5&#34;&gt;&lt;code&gt;c554c3d&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11968&#34;&gt;#11968&lt;/a&gt;
from pytest-dev/backport-11957-to-8.0.x&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/a6851e3459159f94387debf0b357c9b6481a2f48&#34;&gt;&lt;code&gt;a6851e3&lt;/code&gt;&lt;/a&gt;
[8.0.x] main: fix reversed collection order in Session&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/e6f6be3bc9e876f1853fdea68ec49cfc1c4c246d&#34;&gt;&lt;code&gt;e6f6be3&lt;/code&gt;&lt;/a&gt;
[8.0.x] Improve error message when using &lt;a
href=&#34;https://github.com/pytest&#34;&gt;&lt;code&gt;@​pytest&lt;/code&gt;&lt;/a&gt;.fixture twice
(&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11958&#34;&gt;#11958&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/23b91d12de9bcbd0ce965bebefcbcc53a588b438&#34;&gt;&lt;code&gt;23b91d1&lt;/code&gt;&lt;/a&gt;
[8.0.x] Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11941&#34;&gt;#11941&lt;/a&gt;
from bluetech/doctest-parsefactories (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11948&#34;&gt;#11948&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/pytest-dev/pytest/compare/8.0.0...8.0.1&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=pytest&amp;package-manager=pip&amp;previous-version=8.0.0&amp;new-version=8.0.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`4273990`](https://github.com/conijnio/aws-iam-login/commit/427399048207687861cb8b17c272ae54d9eda4bb))

* chore(deps-dev): Bump cryptography from 42.0.0 to 42.0.2 (#166)

Bumps [cryptography](https://github.com/pyca/cryptography) from 42.0.0
to 42.0.2.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst&#34;&gt;cryptography&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;p&gt;42.0.2 - 2024-01-30&lt;/p&gt;
&lt;pre&gt;&lt;code&gt;
* Updated Windows, macOS, and Linux wheels to be compiled with OpenSSL
3.2.1.
* Fixed an issue that prevented the use of Python buffer protocol
objects in
  ``sign`` and ``verify`` methods on asymmetric keys.
* Fixed an issue with incorrect keyword-argument naming with
``EllipticCurvePrivateKey``

:meth:`~cryptography.hazmat.primitives.asymmetric.ec.EllipticCurvePrivateKey.exchange`,
  ``X25519PrivateKey``

:meth:`~cryptography.hazmat.primitives.asymmetric.x25519.X25519PrivateKey.exchange`,
  ``X448PrivateKey``

:meth:`~cryptography.hazmat.primitives.asymmetric.x448.X448PrivateKey.exchange`,
  and ``DHPrivateKey``

:meth:`~cryptography.hazmat.primitives.asymmetric.dh.DHPrivateKey.exchange`.
&lt;p&gt;.. _v42-0-1:&lt;/p&gt;
&lt;p&gt;42.0.1 - 2024-01-24
&lt;/code&gt;&lt;/pre&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Fixed an issue with incorrect keyword-argument naming with
&lt;code&gt;EllipticCurvePrivateKey&lt;/code&gt;

:meth:&lt;code&gt;~cryptography.hazmat.primitives.asymmetric.ec.EllipticCurvePrivateKey.sign&lt;/code&gt;.&lt;/li&gt;
&lt;li&gt;Resolved compatibility issue with loading certain RSA public keys in

:func:&lt;code&gt;~cryptography.hazmat.primitives.serialization.load_pem_public_key&lt;/code&gt;.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;.. _v42-0-0:&lt;/p&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/2202123b50de1b8788f909a3e5afe350c56ad81e&#34;&gt;&lt;code&gt;2202123&lt;/code&gt;&lt;/a&gt;
changelog and version bump 42.0.2 (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10268&#34;&gt;#10268&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/f7032bdd409838f67fc2b93343f897fb5f397d80&#34;&gt;&lt;code&gt;f7032bd&lt;/code&gt;&lt;/a&gt;
bump openssl in CI (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10298&#34;&gt;#10298&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10299&#34;&gt;#10299&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/002e886f16d8857151c09b11dc86b35f2ac9aec3&#34;&gt;&lt;code&gt;002e886&lt;/code&gt;&lt;/a&gt;
Fixes &lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10294&#34;&gt;#10294&lt;/a&gt;
-- correct accidental change to exchange kwarg (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10295&#34;&gt;#10295&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10296&#34;&gt;#10296&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/92fa9f2f606caea5d499c825e832be5bac6f0c23&#34;&gt;&lt;code&gt;92fa9f2&lt;/code&gt;&lt;/a&gt;
support bytes-like consistently across our asym sign/verify APIs (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10260&#34;&gt;#10260&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/1&#34;&gt;#1&lt;/a&gt;...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/6478f7e28be54b51931277235de01b249ceabd96&#34;&gt;&lt;code&gt;6478f7e&lt;/code&gt;&lt;/a&gt;
explicitly support bytes-like for signature/data in RSA sign/verify (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10259&#34;&gt;#10259&lt;/a&gt;)
...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/4bb8596ae02d95bb054dbcf55e8771379dbe0c19&#34;&gt;&lt;code&gt;4bb8596&lt;/code&gt;&lt;/a&gt;
fix the release script (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10233&#34;&gt;#10233&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10254&#34;&gt;#10254&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/337437dc2e62772bde4ad5544f4b1db9ee7572d9&#34;&gt;&lt;code&gt;337437d&lt;/code&gt;&lt;/a&gt;
42.0.1 bump (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10252&#34;&gt;#10252&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/56255de6b2d1a2d2e502b0275231ca81907f33f1&#34;&gt;&lt;code&gt;56255de&lt;/code&gt;&lt;/a&gt;
allow SPKI RSA keys to be parsed even if they have an incorrect
delimiter (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/1&#34;&gt;#1&lt;/a&gt;...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/12f038b38af76e36efe8cef09597010c97647e8f&#34;&gt;&lt;code&gt;12f038b&lt;/code&gt;&lt;/a&gt;
fixes &lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10237&#34;&gt;#10237&lt;/a&gt;
-- correct EC sign parameter name (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10239&#34;&gt;#10239&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10240&#34;&gt;#10240&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/pyca/cryptography/compare/42.0.0...42.0.2&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cryptography&amp;package-manager=pip&amp;previous-version=42.0.0&amp;new-version=42.0.2)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)
You can disable automated security fix PRs for this repo from the
[Security Alerts
page](https://github.com/Nr18/aws-iam-login/network/alerts).

&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`f42cddc`](https://github.com/conijnio/aws-iam-login/commit/f42cddcc845fd30a40b9f1ecc8ea27e864499934))

* chore(deps-dev): Bump twine from 4.0.2 to 5.0.0 (#163) ([`9fd736b`](https://github.com/conijnio/aws-iam-login/commit/9fd736b776c9df8caf9ac5c707d051b0068b574a))

* chore(deps-dev): Bump twine from 4.0.2 to 5.0.0

Bumps [twine](https://github.com/pypa/twine) from 4.0.2 to 5.0.0.
- [Release notes](https://github.com/pypa/twine/releases)
- [Changelog](https://github.com/pypa/twine/blob/main/docs/changelog.rst)
- [Commits](https://github.com/pypa/twine/compare/4.0.2...5.0.0)

---
updated-dependencies:
- dependency-name: twine
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`e3279e1`](https://github.com/conijnio/aws-iam-login/commit/e3279e19b1de6e3ed8c3bd2cabab37c74f80661b))

* chore(deps): Bump boto3 from 1.34.35 to 1.34.40 (#165)

Bumps [boto3](https://github.com/boto/boto3) from 1.34.35 to 1.34.40.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.34.40&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;appsync&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adds
support for new options on GraphqlAPIs, Resolvers and Data Sources for
emitting Amazon CloudWatch metrics for enhanced monitoring of AppSync
APIs.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;cloudwatch&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update
cloudwatch client to latest version&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;neptune-graph&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Adding a new option &amp;quot;parameters&amp;quot; for data plane api
ExecuteQuery to support running parameterized query via SDK.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;route53domains&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds bill contact support for RegisterDomain, TransferDomain,
UpdateDomainContact and GetDomainDetail API.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.39&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;amp&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Overall
documentation updates.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;batch&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This feature
allows Batch to support configuration of repository credentials for jobs
running on ECS&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;braket&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Creating a
job will result in DeviceOfflineException when using an offline device,
and DeviceRetiredException when using a retired device.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;cost-optimization-hub&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] Adding includeMemberAccounts field to the
response of ListEnrollmentStatuses API.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ecs&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Documentation
only update for Amazon ECS.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;iot&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
allows AWS IoT Core users to enable Online Certificate Status Protocol
(OCSP) Stapling for TLS X.509 Server Certificates when creating and
updating AWS IoT Domain Configurations with Custom Domain.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;pricing&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add
Throttling Exception to all APIs.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.38&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;codepipeline&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add
ability to execute pipelines with new parallel &amp;amp; queued execution
modes and add support for triggers with filtering on branches and file
paths.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;quicksight&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] General
Interactions for Visuals; Waterfall Chart Color Configuration;
Documentation Update&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;workspaces&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release introduces User-Decoupling feature. This feature allows
Workspaces Core customers to provision workspaces without providing
users. CreateWorkspaces and DescribeWorkspaces APIs will now take a new
optional parameter &amp;quot;WorkspaceName&amp;quot;.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.37&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;datasync&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] AWS
DataSync now supports manifests for specifying files or objects to
transfer.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;lexv2-models&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update
lexv2-models client to latest version&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;redshift&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
LisRecommendations API to fetch Amazon Redshift Advisor
recommendations.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.36&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;appsync&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Support for
environment variables in AppSync GraphQL APIs&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ecs&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release is
a documentation only update to address customer issues.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;es&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds clear visibility to the customers on the changes that they make on
the domain.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;logs&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds a new field, logGroupArn, to the response of the
logs:DescribeLogGroups action.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;opensearch&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds clear visibility to the customers on the changes that they
make on the domain.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;wafv2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] You can now
delete an API key that you&#39;ve created for use with your CAPTCHA
JavaScript integration API.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/9afe4eef3f028b3e195064d242941517dcbd7cf3&#34;&gt;&lt;code&gt;9afe4ee&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.40&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/23596543d30f410eedba74f3159be132389c0d4c&#34;&gt;&lt;code&gt;2359654&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.40&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/6f6c39b4a86631ecccf113c4f8480c31eca14f8f&#34;&gt;&lt;code&gt;6f6c39b&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/7857384d65e557687c50c48a4e5f682458c43822&#34;&gt;&lt;code&gt;7857384&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.39&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/f8b7ffd355f732acdee03a0fdee92d98260ec9c8&#34;&gt;&lt;code&gt;f8b7ffd&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.39&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/6b674638034188a1b622d9eb317239c981ccf28f&#34;&gt;&lt;code&gt;6b67463&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.39&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/1242e19a61481efc00e467a1cead614fc9004344&#34;&gt;&lt;code&gt;1242e19&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/45aee66d552a8d7281d8ff43e7d153766f4c9192&#34;&gt;&lt;code&gt;45aee66&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.38&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/92042b1ef0ef09cf04da1c275c8a78102e5dca6f&#34;&gt;&lt;code&gt;92042b1&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.38&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/347c1d6d69610709385fe7419955bc61755878b2&#34;&gt;&lt;code&gt;347c1d6&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.38&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.34.35...1.34.40&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.34.35&amp;new-version=1.34.40)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`fccfeed`](https://github.com/conijnio/aws-iam-login/commit/fccfeed3e33ec1b3a1d6ce45a9370ab7eeb692e0))

* chore(deps-dev): Bump black from 24.1.1 to 24.2.0 (#164)

Bumps [black](https://github.com/psf/black) from 24.1.1 to 24.2.0.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/releases&#34;&gt;black&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;24.2.0&lt;/h2&gt;
&lt;h3&gt;Stable style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fixed a bug where comments where mistakenly removed along with
redundant parentheses
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4218&#34;&gt;#4218&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Move the &lt;code&gt;hug_parens_with_braces_and_square_brackets&lt;/code&gt;
feature to the unstable style
due to an outstanding crash and proposed formatting tweaks (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4198&#34;&gt;#4198&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fixed a bug where base expressions caused inconsistent formatting of
** in tenary
expression (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4154&#34;&gt;#4154&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Checking for newline before adding one on docstring that is almost
at the line limit
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4185&#34;&gt;#4185&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Remove redundant parentheses in &lt;code&gt;case&lt;/code&gt; statement
&lt;code&gt;if&lt;/code&gt; guards (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4214&#34;&gt;#4214&lt;/a&gt;).&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix issue where &lt;em&gt;Black&lt;/em&gt; would ignore input files in the
presence of symlinks (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4222&#34;&gt;#4222&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;em&gt;Black&lt;/em&gt; now ignores &lt;code&gt;pyproject.toml&lt;/code&gt; that is
missing a &lt;code&gt;tool.black&lt;/code&gt; section when
discovering project root and configuration. Since &lt;em&gt;Black&lt;/em&gt;
continues to use version
control as an indicator of project root, this is expected to primarily
change behavior
for users in a monorepo setup (desirably). If you wish to preserve
previous behavior,
simply add an empty &lt;code&gt;[tool.black]&lt;/code&gt; to the previously
discovered &lt;code&gt;pyproject.toml&lt;/code&gt;
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4204&#34;&gt;#4204&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Output&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Black will swallow any &lt;code&gt;SyntaxWarning&lt;/code&gt;s or
&lt;code&gt;DeprecationWarning&lt;/code&gt;s produced by the &lt;code&gt;ast&lt;/code&gt;
module when performing equivalence checks (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4189&#34;&gt;#4189&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Add a JSONSchema and provide a validate-pyproject entry-point (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4181&#34;&gt;#4181&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/blob/main/CHANGES.md&#34;&gt;black&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;24.2.0&lt;/h2&gt;
&lt;h3&gt;Stable style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fixed a bug where comments where mistakenly removed along with
redundant parentheses
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4218&#34;&gt;#4218&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Move the &lt;code&gt;hug_parens_with_braces_and_square_brackets&lt;/code&gt;
feature to the unstable style
due to an outstanding crash and proposed formatting tweaks (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4198&#34;&gt;#4198&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fixed a bug where base expressions caused inconsistent formatting of
** in tenary
expression (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4154&#34;&gt;#4154&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Checking for newline before adding one on docstring that is almost
at the line limit
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4185&#34;&gt;#4185&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Remove redundant parentheses in &lt;code&gt;case&lt;/code&gt; statement
&lt;code&gt;if&lt;/code&gt; guards (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4214&#34;&gt;#4214&lt;/a&gt;).&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix issue where &lt;em&gt;Black&lt;/em&gt; would ignore input files in the
presence of symlinks (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4222&#34;&gt;#4222&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;em&gt;Black&lt;/em&gt; now ignores &lt;code&gt;pyproject.toml&lt;/code&gt; that is
missing a &lt;code&gt;tool.black&lt;/code&gt; section when
discovering project root and configuration. Since &lt;em&gt;Black&lt;/em&gt;
continues to use version
control as an indicator of project root, this is expected to primarily
change behavior
for users in a monorepo setup (desirably). If you wish to preserve
previous behavior,
simply add an empty &lt;code&gt;[tool.black]&lt;/code&gt; to the previously
discovered &lt;code&gt;pyproject.toml&lt;/code&gt;
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4204&#34;&gt;#4204&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Output&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Black will swallow any &lt;code&gt;SyntaxWarning&lt;/code&gt;s or
&lt;code&gt;DeprecationWarning&lt;/code&gt;s produced by the &lt;code&gt;ast&lt;/code&gt;
module when performing equivalence checks (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4189&#34;&gt;#4189&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Add a JSONSchema and provide a validate-pyproject entry-point (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4181&#34;&gt;#4181&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/6fdf8a4af28071ed1d079c01122b34c5d587207a&#34;&gt;&lt;code&gt;6fdf8a4&lt;/code&gt;&lt;/a&gt;
Prepare release 24.2.0 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4226&#34;&gt;#4226&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/8af439407c051d55f3221cc93795d20bd9af49c9&#34;&gt;&lt;code&gt;8af4394&lt;/code&gt;&lt;/a&gt;
fix: Don&#39;t remove comments along with parens (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4218&#34;&gt;#4218&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/35e97769190d8c8fe94d9ea2d70d7d88b22a2642&#34;&gt;&lt;code&gt;35e9776&lt;/code&gt;&lt;/a&gt;
Bump pre-commit/action from 3.0.0 to 3.0.1 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4225&#34;&gt;#4225&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/23dfc5b2c3b0694a8c27e58e28439591976aaf94&#34;&gt;&lt;code&gt;23dfc5b&lt;/code&gt;&lt;/a&gt;
Fix ignoring input files for symlink reasons (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4222&#34;&gt;#4222&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/a20100395cf6179a81289452efad1d8e72b19682&#34;&gt;&lt;code&gt;a201003&lt;/code&gt;&lt;/a&gt;
Simplify check for symlinks that resolve outside root (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4221&#34;&gt;#4221&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/dab37a6a1117d690d683121edc4d7c8fb8dd75a7&#34;&gt;&lt;code&gt;dab37a6&lt;/code&gt;&lt;/a&gt;
Remove redundant parentheses in &lt;code&gt;case&lt;/code&gt; statement
&lt;code&gt;if&lt;/code&gt; guards (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4214&#34;&gt;#4214&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/32230e6f5c4bc6bb5c469451e15f3f54d9884b51&#34;&gt;&lt;code&gt;32230e6&lt;/code&gt;&lt;/a&gt;
fix: bug where the doublestar operation had inconsistent formatting. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4154&#34;&gt;#4154&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/7edb50f5a0afc56bb648dc14640ced144366b43a&#34;&gt;&lt;code&gt;7edb50f&lt;/code&gt;&lt;/a&gt;
fix: additional newline added to docstring when the previous line length
is l...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/3e80de3447dee272e9977ab58b1560a669b7b848&#34;&gt;&lt;code&gt;3e80de3&lt;/code&gt;&lt;/a&gt;
Bump furo from 2023.9.10 to 2024.1.29 in /docs (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4211&#34;&gt;#4211&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/a08b480a2f39fb4fc7b210d8b450e33d3879f77d&#34;&gt;&lt;code&gt;a08b480&lt;/code&gt;&lt;/a&gt;
Bump pypa/cibuildwheel from 2.16.4 to 2.16.5 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4212&#34;&gt;#4212&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/psf/black/compare/24.1.1...24.2.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=black&amp;package-manager=pip&amp;previous-version=24.1.1&amp;new-version=24.2.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`a042b7b`](https://github.com/conijnio/aws-iam-login/commit/a042b7beb9adab16a1038f4257e32d219d464762))

* chore(deps-dev): Bump cryptography from 41.0.6 to 42.0.0 (#162)

Bumps [cryptography](https://github.com/pyca/cryptography) from 41.0.6
to 42.0.0.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst&#34;&gt;cryptography&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;p&gt;42.0.0 - 2024-01-22&lt;/p&gt;
&lt;pre&gt;&lt;code&gt;
* **BACKWARDS INCOMPATIBLE:** Dropped support for LibreSSL &amp;lt; 3.7.
* **BACKWARDS INCOMPATIBLE:** Loading a PKCS7 with no content field
using

:func:`~cryptography.hazmat.primitives.serialization.pkcs7.load_pem_pkcs7_certificates`
  or

:func:`~cryptography.hazmat.primitives.serialization.pkcs7.load_der_pkcs7_certificates`
  will now raise a ``ValueError`` rather than return an empty list.
* Parsing SSH certificates no longer permits malformed critical options
with
  values, as documented in the 41.0.2 release notes.
* Updated Windows, macOS, and Linux wheels to be compiled with OpenSSL
3.2.0.
* Updated the minimum supported Rust version (MSRV) to 1.63.0, from
1.56.0.
* We now publish both ``py37`` and ``py39`` ``abi3`` wheels. This should
resolve some errors relating to initializing a module multiple times per
  process.
* Support
:class:`~cryptography.hazmat.primitives.asymmetric.padding.PSS` for
X.509 certificate signing requests and certificate revocation lists with
the
  keyword-only argument ``rsa_padding`` on the ``sign`` methods for
  :class:`~cryptography.x509.CertificateSigningRequestBuilder` and
  :class:`~cryptography.x509.CertificateRevocationListBuilder`.
* Added support for obtaining X.509 certificate signing request
signature
  algorithm parameters (including PSS) via

:meth:`~cryptography.x509.CertificateSigningRequest.signature_algorithm_parameters`.
* Added support for obtaining X.509 certificate revocation list
signature
  algorithm parameters (including PSS) via

:meth:`~cryptography.x509.CertificateRevocationList.signature_algorithm_parameters`.
* Added ``mgf`` property to
  :class:`~cryptography.hazmat.primitives.asymmetric.padding.PSS`.
* Added ``algorithm`` and ``mgf`` properties to
  :class:`~cryptography.hazmat.primitives.asymmetric.padding.OAEP`.
* Added the following properties that return timezone-aware ``datetime``
objects:
  :meth:`~cryptography.x509.Certificate.not_valid_before_utc`,
  :meth:`~cryptography.x509.Certificate.not_valid_after_utc`,
  :meth:`~cryptography.x509.RevokedCertificate.revocation_date_utc`,
  :meth:`~cryptography.x509.CertificateRevocationList.next_update_utc`,
  :meth:`~cryptography.x509.CertificateRevocationList.last_update_utc`.
These are timezone-aware variants of existing properties that return
naïve
  ``datetime`` objects.
* Deprecated the following properties that return naïve ``datetime``
objects:
  :meth:`~cryptography.x509.Certificate.not_valid_before`,
  :meth:`~cryptography.x509.Certificate.not_valid_after`,
  :meth:`~cryptography.x509.RevokedCertificate.revocation_date`,
  :meth:`~cryptography.x509.CertificateRevocationList.next_update`,
  :meth:`~cryptography.x509.CertificateRevocationList.last_update`
  in favor of the new timezone-aware variants mentioned above.
* Added support for
  :class:`~cryptography.hazmat.primitives.ciphers.algorithms.ChaCha20`
  on LibreSSL.
* Added support for RSA PSS signatures in PKCS7 with
&amp;lt;/tr&amp;gt;&amp;lt;/table&amp;gt; 
&lt;/code&gt;&lt;/pre&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/4e64baf360a3a89bd92582f59344c12b5c0bd3fd&#34;&gt;&lt;code&gt;4e64baf&lt;/code&gt;&lt;/a&gt;
42.0.0 version bump (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10232&#34;&gt;#10232&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/7cb13a3bc91b7537c6231674fb5b0d2132a7edbe&#34;&gt;&lt;code&gt;7cb13a3&lt;/code&gt;&lt;/a&gt;
we&#39;ll ship 3.2.0 for 42 (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/9951&#34;&gt;#9951&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/605c74e41c75edc717f21afaa5e6a0eee9863a10&#34;&gt;&lt;code&gt;605c74e&lt;/code&gt;&lt;/a&gt;
Bump x509-limbo and/or wycheproof in CI (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10231&#34;&gt;#10231&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/97578b98ffc417864e07d0ff9b76c02d2cb4e6da&#34;&gt;&lt;code&gt;97578b9&lt;/code&gt;&lt;/a&gt;
Bump BoringSSL and/or OpenSSL in CI (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10230&#34;&gt;#10230&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/972a7b5896a6047ea43a86db87820ab474d898ff&#34;&gt;&lt;code&gt;972a7b5&lt;/code&gt;&lt;/a&gt;
verification: add test_verify_tz_aware (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10229&#34;&gt;#10229&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/41daf2d86dd9bf18081802fa5d851a7953810786&#34;&gt;&lt;code&gt;41daf2d&lt;/code&gt;&lt;/a&gt;
Migrate PKCS7 backend to Rust (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10228&#34;&gt;#10228&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/d54093e62e7e68c02efbb4d6a09162ddb39bf72f&#34;&gt;&lt;code&gt;d54093e&lt;/code&gt;&lt;/a&gt;
Remove some skips in tests that aren&#39;t needed anymore (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10223&#34;&gt;#10223&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/71929bd91f34213b9f4a3a0a493c218c35fa25eb&#34;&gt;&lt;code&gt;71929bd&lt;/code&gt;&lt;/a&gt;
Remove binding that&#39;s not used anymore (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10224&#34;&gt;#10224&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/7ea4b89cea553ce0f641ed29e1ce2e3e34278f1d&#34;&gt;&lt;code&gt;7ea4b89&lt;/code&gt;&lt;/a&gt;
fixed formatting in changelog (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10225&#34;&gt;#10225&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/410f4a1ee4cbf46fe7e969bb48fccf261f74bbcd&#34;&gt;&lt;code&gt;410f4a1&lt;/code&gt;&lt;/a&gt;
Allow brainpool on libressl (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/10222&#34;&gt;#10222&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/pyca/cryptography/compare/41.0.6...42.0.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cryptography&amp;package-manager=pip&amp;previous-version=41.0.6&amp;new-version=42.0.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)
You can disable automated security fix PRs for this repo from the
[Security Alerts
page](https://github.com/Nr18/aws-iam-login/network/alerts).

&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`4a9e183`](https://github.com/conijnio/aws-iam-login/commit/4a9e18313269b561ffade95f500ae7f19197fa3a))

* chore(deps): Bump boto3 from 1.34.30 to 1.34.35 (#161)

Bumps [boto3](https://github.com/boto/boto3) from 1.34.30 to 1.34.35.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.34.35&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;glue&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Introduce
Catalog Encryption Role within Glue Data Catalog Settings. Introduce
SASL/PLAIN as an authentication method for Glue Kafka connections&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;workspaces&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added
definitions of various WorkSpace states&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.34&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;dynamodb&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Any number
of users can execute up to 50 concurrent restores (any type of restore)
in a given account.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;sagemaker&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Amazon
SageMaker Canvas adds GenerativeAiSettings support for
CanvasAppSettings.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;endpoint-rules&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update endpoint-rules client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.33&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;cognito-idp&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added
CreateIdentityProvider and UpdateIdentityProvider details for new SAML
IdP features&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ivs&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
introduces a new resource Playback Restriction Policy which can be used
to geo-restrict or domain-restrict channel stream playback when
associated with a channel. New APIs to support this resource were
introduced in the form of Create/Delete/Get/Update/List.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;managedblockchain-query&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] This release adds support for transactions that
have not reached finality. It also removes support for the status
property from the response of the GetTransaction operation. You can use
the confirmationStatus and executionStatus properties to determine the
status of the transaction.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;mediaconvert&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release includes support for broadcast-mixed audio description
tracks.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;neptune-graph&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Adding new APIs in SDK for Amazon Neptune Analytics. These APIs include
operations to execute, cancel, list queries and get the graph
summary.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.32&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;cloudformation&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
CloudFormation IaC generator allows you to scan existing resources in
your account and select resources to generate a template for a new or
existing CloudFormation stack.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;elbv2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update elbv2
client to latest version&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;glue&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update page
size limits for GetJobRuns and GetTriggers APIs.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ssm&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds an optional Duration parameter to StateManager Associations. This
allows customers to specify how long an apply-only-on-cron association
execution should run. Once the specified Duration is out all the ongoing
cancellable commands or automations are cancelled.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.31&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;datazone&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add new
skipDeletionCheck to DeleteDomain. Add new skipDeletionCheck to
DeleteProject which also automatically deletes dependent objects&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;route53&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update the
SDKs for text changes in the APIs.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/f4d6e2932e7cbe35f9165cd61070aac9e3163edc&#34;&gt;&lt;code&gt;f4d6e29&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.35&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/ae08129b8f853b2dc8e2c57c4e8e80bad10f441e&#34;&gt;&lt;code&gt;ae08129&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.35&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/622a79b0e4dca515acdc4b9dbe372920b661eb21&#34;&gt;&lt;code&gt;622a79b&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/6ae396d6d2f321cc7e7a625118c9ed03fd09f06f&#34;&gt;&lt;code&gt;6ae396d&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.34&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/271aa9855ccbbfa1ffbc66476f07626f3ff06199&#34;&gt;&lt;code&gt;271aa98&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.34&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/de767ae74008bfbbcf4e3166f2b47bf6ceb05a84&#34;&gt;&lt;code&gt;de767ae&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.34&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/7d20b1556d9aba544dd68f6344af63d8601fb29f&#34;&gt;&lt;code&gt;7d20b15&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/c8cb414b5c8bdb2c38d92e6c9c15085f53584616&#34;&gt;&lt;code&gt;c8cb414&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.33&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/07dd6f7f38d2b85222e63f210ad8ea67ad4e5984&#34;&gt;&lt;code&gt;07dd6f7&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.33&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/f6294f7966ebd4bf855034c4cad2a32ee11314f3&#34;&gt;&lt;code&gt;f6294f7&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.33&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.34.30...1.34.35&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.34.30&amp;new-version=1.34.35)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`53ea2c5`](https://github.com/conijnio/aws-iam-login/commit/53ea2c5c425ea741d4b00c96f5794f301565c37c))

* chore(deps-dev): Bump black from 23.12.1 to 24.1.1 (#159) ([`6653193`](https://github.com/conijnio/aws-iam-login/commit/665319387bf9cc110c3cb874a9e042a0d98f2e85))

* chore(deps-dev): Bump black from 23.12.1 to 24.1.1

Bumps [black](https://github.com/psf/black) from 23.12.1 to 24.1.1.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/23.12.1...24.1.1)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`b7ef88a`](https://github.com/conijnio/aws-iam-login/commit/b7ef88a289acb545c4e65380b00d72776f832b17))

* chore(deps-dev): Bump pytest from 7.4.4 to 8.0.0 (#158) ([`7de44fb`](https://github.com/conijnio/aws-iam-login/commit/7de44fb06e874350c0a8994d756e68a91d999bb3))

* chore(deps): Bump boto3 from 1.34.24 to 1.34.30 (#160)

Bumps [boto3](https://github.com/boto/boto3) from 1.34.24 to 1.34.30.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.34.30&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;autoscaling&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] EC2
Auto Scaling customers who use attribute based instance-type selection
can now intuitively define their Spot instances price protection limit
as a percentage of the lowest priced On-Demand instance type.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;comprehend&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Comprehend PII analysis now supports Spanish input documents.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ec2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] EC2 Fleet
customers who use attribute based instance-type selection can now
intuitively define their Spot instances price protection limit as a
percentage of the lowest priced On-Demand instance type.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;mwaa&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds MAINTENANCE environment status for Amazon MWAA environments.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;rds&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Introduced
support for the InsufficientDBInstanceCapacityFault error in the RDS
RestoreDBClusterFromSnapshot and RestoreDBClusterToPointInTime API
methods. This provides enhanced error handling, ensuring a more robust
experience.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;snowball&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Modified
description of createaddress to include direction to add path when
providing a JSON file.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.29&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;connect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update list
and string length limits for predefined attributes.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;inspector2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds ECR container image scanning based on their
lastRecordedPullTime.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;sagemaker&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Amazon
SageMaker Automatic Model Tuning now provides an API to programmatically
delete tuning jobs.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.28&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;acm-pca&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] AWS Private
CA now supports an option to omit the CDP extension from issued
certificates, when CRL revocation is enabled.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;lightsail&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds support for IPv6-only instance plans.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.27&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;ec2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Introduced a
new clientToken request parameter on CreateNetworkAcl and
CreateRouteTable APIs. The clientToken parameter allows idempotent
operations on the APIs.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ecs&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Documentation
updates for Amazon ECS.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;outposts&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
DeviceSerialNumber parameter is now optional in StartConnection API&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;rds&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds support for Aurora Limitless Database.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;storagegateway&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add
DeprecationDate and SoftwareVersion to response of ListGateways.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.26&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;inspector2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds support for CIS scans on EC2 instances.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.25&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;enhancement:documentation: [&lt;code&gt;botocore&lt;/code&gt;] Updates the
GitHub issue creation link in our README&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/a1ac69936c14503310d9d8fbf2554c7410d12124&#34;&gt;&lt;code&gt;a1ac699&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.30&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/3f7cb1cff827cf67ae02a7966c7b02a37b645e93&#34;&gt;&lt;code&gt;3f7cb1c&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.30&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/47365d2a7c24b736b82fa833260fcc8389043331&#34;&gt;&lt;code&gt;47365d2&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/45be5e9f0994b86f3ea6ab50ed3b0d6e9a9d96bf&#34;&gt;&lt;code&gt;45be5e9&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.29&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/6bbdf83ee00b749587f0fe54778fbec5411147b5&#34;&gt;&lt;code&gt;6bbdf83&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.29&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/40e58d41e58cf260744868062767a314e1c68d15&#34;&gt;&lt;code&gt;40e58d4&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.29&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/c0f6375ee50d96176b8c0d25b435f63cddc92969&#34;&gt;&lt;code&gt;c0f6375&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/8ef5c71dce3898f7920c547d9d6b54ca9b70a30d&#34;&gt;&lt;code&gt;8ef5c71&lt;/code&gt;&lt;/a&gt;
Minor GitHub workflow changes (&lt;a
href=&#34;https://redirect.github.com/boto/boto3/issues/3998&#34;&gt;#3998&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/4ab369abbb2beb653432972996c3bb57430caf49&#34;&gt;&lt;code&gt;4ab369a&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.28&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/038a03fe068de4aa5f129a3e455b6c6b47a009d9&#34;&gt;&lt;code&gt;038a03f&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.28&#39; into develop&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.34.24...1.34.30&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.34.24&amp;new-version=1.34.30)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`2317146`](https://github.com/conijnio/aws-iam-login/commit/2317146b4c54d1a0e6941aacae7f884462c3f1cb))

* chore(deps-dev): Bump pytest from 7.4.4 to 8.0.0

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.4.4 to 8.0.0.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.4.4...8.0.0)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`afef119`](https://github.com/conijnio/aws-iam-login/commit/afef119e9f0798b01f03ce73822c30fed70accf8))

* chore(deps): Bump boto3 from 1.34.19 to 1.34.24 (#157)

Bumps [boto3](https://github.com/boto/boto3) from 1.34.19 to 1.34.24.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.34.24&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;appconfigdata&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Fix
FIPS Endpoints in aws-us-gov.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;cloud9&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Doc-only
update around removing AL1 from list of available AMIs for Cloud9&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;cloudfront-keyvaluestore&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] This release improves upon the
DescribeKeyValueStore API by returning two additional fields, Status of
the KeyValueStore and the FailureReason in case of failures during
creation of KeyValueStore.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;connectcases&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds the ability to view audit history on a case and introduces
a new parameter, performedBy, for CreateCase and UpdateCase API&#39;s.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ec2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Documentation
updates for Amazon EC2.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ecs&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds support for Transport Layer Security (TLS) and Configurable Timeout
to ECS Service Connect. TLS facilitates privacy and data security for
inter-service communications, while Configurable Timeout allows
customized per-request timeout and idle timeout for Service Connect
services.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;finspace&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Allow
customer to set zip default through command line arguments.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;organizations&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Doc
only update for quota increase change&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;rds&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Introduced
support for the InsufficientDBInstanceCapacityFault error in the RDS
CreateDBCluster API method. This provides enhanced error handling,
ensuring a more robust experience when creating database clusters with
insufficient instance capacity.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;endpoint-rules&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update endpoint-rules client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.23&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;athena&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Introducing
new NotebookS3LocationUri parameter to Athena ImportNotebook API.
Payload is no longer required and either Payload or
NotebookS3LocationUri needs to be provided (not both) for a successful
ImportNotebook API call. If both are provided, an
InvalidRequestException will be thrown.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;codebuild&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Release
CodeBuild Reserved Capacity feature&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;dynamodb&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds support for including ApproximateCreationDateTimePrecision
configurations in EnableKinesisStreamingDestination API, adds the same
as an optional field in the response of
DescribeKinesisStreamingDestination, and adds support for a new
UpdateKinesisStreamingDestination API.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;qconnect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Increased
Quick Response name max length to 100&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.22&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;b2bi&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Increasing
TestMapping inputFileContent file size limit to 5MB and adding file size
limit 250KB for TestParsing input file. This release also includes
exposing InternalServerException for Tag APIs.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;cloudtrail&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds a new API ListInsightsMetricData to retrieve metric data
from CloudTrail Insights.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;connect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
GetMetricDataV2 now supports 3 groupings&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;drs&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Removed invalid
and unnecessary default values.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;firehose&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Allow
support for Snowflake as a Kinesis Data Firehose delivery
destination.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;sagemaker-featurestore-runtime&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] Increase BatchGetRecord limits from 10 items to
100 items&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.21&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;dynamodb&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Updating
note for enabling streams for UpdateTable.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;keyspaces&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds support for Multi-Region Replication with provisioned
tables, and Keyspaces auto scaling APIs&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.20&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;iot&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Revert release
of LogTargetTypes&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;iotfleetwise&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Updated APIs: SignalNodeType query parameter has been added to
ListSignalCatalogNodesRequest and ListVehiclesResponse has been extended
with attributes field.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;macie2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds support for analyzing Amazon S3 objects that are encrypted using
dual-layer server-side encryption with AWS KMS keys (DSSE-KMS). It also
adds support for reporting DSSE-KMS details in statistics and metadata
about encryption settings for S3 buckets and objects.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;payment-cryptography&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] Provide an additional option for key exchange
using RSA wrap/unwrap in addition to tr-34/tr-31 in ImportKey and
ExportKey operations. Added new key usage (type)
TR31_M1_ISO_9797_1_MAC_KEY, for use with Generate/VerifyMac dataplane
operations with ISO9797 Algorithm 1 MAC calculations.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;personalize-runtime&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Documentation updates for Amazon Personalize&lt;/li&gt;
&lt;/ul&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/63b461731e60605055d5065c63efa04ecc292ff0&#34;&gt;&lt;code&gt;63b4617&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.24&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/7dca36afdfd8aebe7f06dc1c0993b906fa0ce2fe&#34;&gt;&lt;code&gt;7dca36a&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.24&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/a539345316741038b2ca2385dd4a635bbebf93f2&#34;&gt;&lt;code&gt;a539345&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/e209e660ab483a1f2bc2f46bbe508cb91e254a67&#34;&gt;&lt;code&gt;e209e66&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.23&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/710402a74b97d34a450b4d1e00c7ec9bfd64ac5d&#34;&gt;&lt;code&gt;710402a&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.23&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/d9931137df853dd9a18d09d232f117ac1abf94d1&#34;&gt;&lt;code&gt;d993113&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.23&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/8ecc67a1e948450caafea5730f97008fd8c2aba0&#34;&gt;&lt;code&gt;8ecc67a&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/2c65eab9864368b0ede75f59f3d54d8bee6594ee&#34;&gt;&lt;code&gt;2c65eab&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.22&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/8f855b38f3ee24bd9dc12a5454ebe9eaef789fc6&#34;&gt;&lt;code&gt;8f855b3&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.22&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/c1faee7bed743bc93445b692745e738206bb70cc&#34;&gt;&lt;code&gt;c1faee7&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.22&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.34.19...1.34.24&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.34.19&amp;new-version=1.34.24)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`77ae8cc`](https://github.com/conijnio/aws-iam-login/commit/77ae8cccb3a7deec3dba58134b7feed5a11e622c))

* chore(deps): Bump boto3 from 1.34.15 to 1.34.19 (#156)

Bumps [boto3](https://github.com/boto/boto3) from 1.34.15 to 1.34.19.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.34.19&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;sagemaker&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release will have ValidationException thrown if certain invalid app
types are provided. The release will also throw ValidationException if
more than 10 account ids are provided in VpcOnlyTrustedAccounts.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.18&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;connect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Supervisor
Barge for Chat is now supported through the MonitorContact API.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;connectparticipant&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Introduce new Supervisor participant role&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;location&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Location
SDK documentation update. Added missing fonts to the MapConfiguration
data type. Updated note for the SubMunicipality property in the place
data type.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;mwaa&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This Amazon
MWAA feature release includes new fields in CreateWebLoginToken response
model. The new fields IamIdentity and AirflowIdentity will let you match
identifications, as the Airflow identity length is currently hashed to
64 characters.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;s3control&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] S3 On
Outposts team adds dualstack endpoints support for S3Control and
S3Outposts API calls.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;supplychain&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release includes APIs CreateBillOfMaterialsImportJob and
GetBillOfMaterialsImportJob.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;transfer&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] AWS
Transfer Family now supports static IP addresses for SFTP &amp;amp; AS2
connectors and for async MDNs on AS2 servers.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;endpoint-rules&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update endpoint-rules client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.17&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;ec2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds support for adding an ElasticBlockStorage volume configurations in
ECS RunTask/StartTask/CreateService/UpdateService APIs. The
configuration allows for attaching EBS volumes to ECS Tasks.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ecs&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds support for adding an ElasticBlockStorage volume configurations in
ECS RunTask/StartTask/CreateService/UpdateService APIs. The
configuration allows for attaching EBS volumes to ECS Tasks.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;events&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update
events client to latest version&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;iot&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add
ConflictException to Update APIs of AWS IoT Software Package
Catalog&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;iotfleetwise&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] The
following dataTypes have been removed: CUSTOMER_DECODED_INTERFACE in
NetworkInterfaceType; CUSTOMER_DECODED_SIGNAL_INFO_IS_NULL in
SignalDecoderFailureReason;
CUSTOMER_DECODED_SIGNAL_NETWORK_INTERFACE_INFO_IS_NULL in
NetworkInterfaceFailureReason; CUSTOMER_DECODED_SIGNAL in
SignalDecoderType&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;secretsmanager&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Doc
only update for Secrets Manager&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;workspaces&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added
AWS Workspaces RebootWorkspaces API - Extended Reboot documentation
update&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.16&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;connectcampaigns&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Minor pattern updates for Campaign and Dial Request API fields.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;location&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds API support for custom layers for the maps service APIs:
CreateMap, UpdateMap, DescribeMap.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;logs&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add support
for account level subscription filter policies to PutAccountPolicy,
DescribeAccountPolicies, and DeleteAccountPolicy APIs. Additionally,
PutAccountPolicy has been modified with new optional
&amp;quot;selectionCriteria&amp;quot; parameter for resource selection.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;qconnect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
QueryAssistant and GetRecommendations will be discontinued starting June
1, 2024. To receive generative responses after March 1, 2024 you will
need to create a new Assistant in the Connect console and integrate the
Amazon Q in Connect JavaScript library (amazon-q-connectjs) into your
applications.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;redshift-serverless&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Updates to ConfigParameter for RSS workgroup, removal of
use_fips_ssl&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;route53&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Route53 now
supports geoproximity routing in AWS regions&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;wisdom&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
QueryAssistant and GetRecommendations will be discontinued starting June
1, 2024. To receive generative responses after March 1, 2024 you will
need to create a new Assistant in the Connect console and integrate the
Amazon Q in Connect JavaScript library (amazon-q-connectjs) into your
applications.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/1d7b3fbf03f26ed4563fa95f3a737a8fabaa819a&#34;&gt;&lt;code&gt;1d7b3fb&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.19&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/dca34ab35adaabb6dbdd0f38ab11554274d866f7&#34;&gt;&lt;code&gt;dca34ab&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.19&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/5b45465823ba6f942a8a1c4e22caf6e6da38f06c&#34;&gt;&lt;code&gt;5b45465&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/9556ce04f2ac1f8c8cac29527ad2fa48ce780230&#34;&gt;&lt;code&gt;9556ce0&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.18&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/363eca9d042c3b0a9b3c8b5cce35e783d950f790&#34;&gt;&lt;code&gt;363eca9&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.18&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/3cd4d497cccacbaf33658f6c64bb8e152876086f&#34;&gt;&lt;code&gt;3cd4d49&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.18&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/e618bd497eb125b681d1a62bca6ebc4a64c0ce50&#34;&gt;&lt;code&gt;e618bd4&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/4791dc2e718c822daed5537b17dc3840cda84b85&#34;&gt;&lt;code&gt;4791dc2&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.17&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/5e9197ec87e4a6cb7c666a02eb8689e0b0b36709&#34;&gt;&lt;code&gt;5e9197e&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.17&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/4876f600c44611d6028fa32cef58a8205733bf6d&#34;&gt;&lt;code&gt;4876f60&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.17&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.34.15...1.34.19&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.34.15&amp;new-version=1.34.19)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`52693ff`](https://github.com/conijnio/aws-iam-login/commit/52693ff0c4f859fd6994bcb648122cfe068dfe78))

* chore(deps): Bump boto3 from 1.34.11 to 1.34.15 (#155)

Bumps [boto3](https://github.com/boto/boto3) from 1.34.11 to 1.34.15.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.34.15&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;codebuild&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Aws
CodeBuild now supports new compute type BUILD_GENERAL1_XLARGE&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ec2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Amazon EC2 R7iz
bare metal instances are powered by custom 4th generation Intel Xeon
Scalable processors.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;route53resolver&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
This release adds support for query type configuration on firewall rules
that enables customers for granular action (ALLOW, ALERT, BLOCK) by DNS
query type.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.14&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;connect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Minor trait
updates for User APIs&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;kms&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Documentation
updates for AWS Key Management Service (KMS).&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;redshift-serverless&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
use_fips_ssl and require_ssl parameter support for Workgroup,
UpdateWorkgroup, and CreateWorkgroup&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.13&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;config&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Updated
ResourceType enum with new resource types onboarded by AWS Config in
November and December 2023.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;docdb&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adding
PerformanceInsightsEnabled and PerformanceInsightsKMSKeyId fields to
DescribeDBInstances Response.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ecs&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds support for managed instance draining which facilitates graceful
termination of Amazon ECS instances.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;es&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds support for new or existing Amazon OpenSearch domains to enable TLS
1.3 or TLS 1.2 with perfect forward secrecy cipher suites for domain
endpoints.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;lightsail&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds support to set up an HTTPS endpoint on an instance.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;opensearch&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds support for new or existing Amazon OpenSearch domains to
enable TLS 1.3 or TLS 1.2 with perfect forward secrecy cipher suites for
domain endpoints.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;sagemaker&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adding
support for provisioned throughput mode for SageMaker Feature
Groups&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;servicecatalog&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Added Idempotency token support to Service Catalog
AssociateServiceActionWithProvisioningArtifact,
DisassociateServiceActionFromProvisioningArtifact, DeleteServiceAction
API&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;endpoint-rules&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update endpoint-rules client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.12&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;connect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Amazon
Connect, Contact Lens Evaluation API increase evaluation notes max
length to 3072.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;mediaconvert&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release includes video engine updates including HEVC improvements,
support for ingesting VP9 encoded video in MP4 containers, and support
for user-specified 3D LUTs.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/12425cda7457bda860e4420860f5e9e1a9c235b9&#34;&gt;&lt;code&gt;12425cd&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.15&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/54bd94e25ed35e96759bc6a9c7752c251e34499c&#34;&gt;&lt;code&gt;54bd94e&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.15&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/8a568bfa35c08f085204a1f35bc637208ec8a309&#34;&gt;&lt;code&gt;8a568bf&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/bb90483603888a0c1096fb05985728352fc24b90&#34;&gt;&lt;code&gt;bb90483&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.14&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/cf8654aeb591aff537f123b42a091ebf2c8f9c11&#34;&gt;&lt;code&gt;cf8654a&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.14&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/32f0017ac757aeacf6e42b2dce3acf944df7a246&#34;&gt;&lt;code&gt;32f0017&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.14&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/09a970f753bb7d49426e2b2ff3f99ff8084e7c65&#34;&gt;&lt;code&gt;09a970f&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/1f863eca122ed44bbc2758da5da988273299cb19&#34;&gt;&lt;code&gt;1f863ec&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.13&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/c36a05f67af5b3cb0c925ea1cc104882ad2988e5&#34;&gt;&lt;code&gt;c36a05f&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.13&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/fac1271d21e46fa299f4bba1394ae302f71c7cd9&#34;&gt;&lt;code&gt;fac1271&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.13&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.34.11...1.34.15&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.34.11&amp;new-version=1.34.15)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`98dcddd`](https://github.com/conijnio/aws-iam-login/commit/98dcddd2b97518ec35c1255c6ab805002095289f))

* chore(deps-dev): Bump pytest from 7.4.3 to 7.4.4 (#154)

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.4.3 to
7.4.4.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pytest-dev/pytest/releases&#34;&gt;pytest&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;pytest 7.4.4 (2023-12-31)&lt;/h2&gt;
&lt;h2&gt;Bug Fixes&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11140&#34;&gt;#11140&lt;/a&gt;:
Fix non-string constants at the top of file being detected as docstrings
on Python&amp;gt;=3.8.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11572&#34;&gt;#11572&lt;/a&gt;:
Handle an edge case where &lt;code&gt;sys.stderr&lt;/code&gt;{.interpreted-text
role=&amp;quot;data&amp;quot;} and &lt;code&gt;sys.__stderr__&lt;/code&gt;{.interpreted-text
role=&amp;quot;data&amp;quot;} might already be closed when
&lt;code&gt;faulthandler&lt;/code&gt;{.interpreted-text role=&amp;quot;ref&amp;quot;} is
tearing down.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11710&#34;&gt;#11710&lt;/a&gt;:
Fixed tracebacks from collection errors not getting pruned.&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/7966&#34;&gt;#7966&lt;/a&gt;:
Removed unhelpful error message from assertion rewrite mechanism when
exceptions are raised in &lt;code&gt;__iter__&lt;/code&gt; methods. Now they are
treated un-iterable instead.&lt;/li&gt;
&lt;/ul&gt;
&lt;h2&gt;Improved Documentation&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11091&#34;&gt;#11091&lt;/a&gt;:
Updated documentation to refer to hyphenated options: replaced
&lt;code&gt;--junitxml&lt;/code&gt; with &lt;code&gt;--junit-xml&lt;/code&gt; and
&lt;code&gt;--collectonly&lt;/code&gt; with &lt;code&gt;--collect-only&lt;/code&gt;.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/33f694f4b30c5c502f21f81cb8ab907b12ad2f65&#34;&gt;&lt;code&gt;33f694f&lt;/code&gt;&lt;/a&gt;
Prepare release version 7.4.4&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/76c107c463afcaddf74ca48252614728c6829ea7&#34;&gt;&lt;code&gt;76c107c&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11751&#34;&gt;#11751&lt;/a&gt;
from bluetech/backport-11143-to-7.4.x&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/531d76daa4a871df5b2a46cae132851c29abf027&#34;&gt;&lt;code&gt;531d76d&lt;/code&gt;&lt;/a&gt;
[7.4.x] Improve reporting from &lt;strong&gt;iter&lt;/strong&gt; exceptions (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11749&#34;&gt;#11749&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/a0f58fa9e7f9b09b212ed491464be5df9b80fc0b&#34;&gt;&lt;code&gt;a0f58fa&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11143&#34;&gt;#11143&lt;/a&gt;
from tushar-deepsource/patch-1&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/b1f3387d42571090ee4a35ec1945765b7f2ffae8&#34;&gt;&lt;code&gt;b1f3387&lt;/code&gt;&lt;/a&gt;
[7.4.x] &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11091&#34;&gt;#11091&lt;/a&gt;:
documentation should use hypthonated properties (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11750&#34;&gt;#11750&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/2cdd619bf49ee7c5306dc70dcbf71090839ea985&#34;&gt;&lt;code&gt;2cdd619&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11747&#34;&gt;#11747&lt;/a&gt;
from pytest-dev/backport-11711-to-7.4.x&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/d06c05bd23ea6af8e07fd944e56c58b64375b724&#34;&gt;&lt;code&gt;d06c05b&lt;/code&gt;&lt;/a&gt;
[7.4.x] nodes: fix tracebacks from collection errors are not getting
pruned&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/5582bfcddf78929f7979c5023b167b333e1c2dd9&#34;&gt;&lt;code&gt;5582bfc&lt;/code&gt;&lt;/a&gt;
[7.4.x] Improves clarity in Sphinx documentation for function signature.
(&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11&#34;&gt;#11&lt;/a&gt;...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/13024efd7afdbae80ce70d27295d9bbe62670cb8&#34;&gt;&lt;code&gt;13024ef&lt;/code&gt;&lt;/a&gt;
[7.4.x] Fix for operation on closed file in faulthandler teardown (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11631&#34;&gt;#11631&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/a40dacf6577ae990740e10572582538dfaf357b6&#34;&gt;&lt;code&gt;a40dacf&lt;/code&gt;&lt;/a&gt;
[7.4.x] XFAIL TestLocalPath.test_make_numbered_dir_multiprocess_safe (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11616&#34;&gt;#11616&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/pytest-dev/pytest/compare/7.4.3...7.4.4&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=pytest&amp;package-manager=pip&amp;previous-version=7.4.3&amp;new-version=7.4.4)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`1f8eb98`](https://github.com/conijnio/aws-iam-login/commit/1f8eb98e80886776769ac156fddf7c3ea30cc8cc))

* chore(deps): Bump boto3 from 1.34.7 to 1.34.11 (#153)

Bumps [boto3](https://github.com/boto/boto3) from 1.34.7 to 1.34.11.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.34.11&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;apprunner&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] AWS App
Runner adds Python 3.11 and Node.js 18 runtimes.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;location&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release introduces a new parameter to bypasses an API key&#39;s expiry
conditions and delete the key.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;quicksight&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add
LinkEntityArn support for different partitions; Add
UnsupportedUserEditionException in UpdateDashboardLinks API; Add support
for New Reader Experience Topics&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.10&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;codestar-connections&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] New integration with the GitLab self-managed
provider type.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;kinesis-video-archived-media&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] NoDataRetentionException thrown when GetImages
requested for a Stream that does not retain data (that is, has a
DataRetentionInHours of 0).&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;sagemaker&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Amazon
SageMaker Studio now supports Docker access from within app
container&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.9&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;emr&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update emr
client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.8&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;iam&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Documentation
updates for AWS Identity and Access Management (IAM).&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;endpoint-rules&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update endpoint-rules client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/270df835c7a926e50f29c7a68b6cd9dca77346ff&#34;&gt;&lt;code&gt;270df83&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.11&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/136ae4544c99937591b3e16ba7543540abb4ecff&#34;&gt;&lt;code&gt;136ae45&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.11&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/4c94545c07de45378b7f8dd7b3878577f5326335&#34;&gt;&lt;code&gt;4c94545&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/5cd33d7ff59cb2ceb7f350a38beffe37bc308917&#34;&gt;&lt;code&gt;5cd33d7&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.10&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/1179f949c55c1cd8f10e761360f9fe2989b73199&#34;&gt;&lt;code&gt;1179f94&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.10&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/af123ecd2abb0c83dd8fc91eefbdc988b2256cc1&#34;&gt;&lt;code&gt;af123ec&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.10&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/587d4e49f17ff3db60dc328db164209fd051f476&#34;&gt;&lt;code&gt;587d4e4&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/48a0ee15f789c9c60d24f05e63f5caf8a0f2e3af&#34;&gt;&lt;code&gt;48a0ee1&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.9&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/67af4087b42c524886dd8b20da25246b49d18d1f&#34;&gt;&lt;code&gt;67af408&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.9&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/ff818f1f7d43edb97185ee03ef9f022a3eac2125&#34;&gt;&lt;code&gt;ff818f1&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.9&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.34.7...1.34.11&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.34.7&amp;new-version=1.34.11)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`b99d66e`](https://github.com/conijnio/aws-iam-login/commit/b99d66e6c6e0111ddcd41c5a22f30168141fc324))

* chore(deps): Bump boto3 from 1.34.3 to 1.34.7 (#152)

Bumps [boto3](https://github.com/boto/boto3) from 1.34.3 to 1.34.7.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.34.7&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;bedrock-agent&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Adding Claude 2.1 support to Bedrock Agents&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;glue&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds additional configurations for Query Session Context on the
following APIs: GetUnfilteredTableMetadata,
GetUnfilteredPartitionMetadata, GetUnfilteredPartitionsMetadata.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;lakeformation&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds additional configurations on
GetTemporaryGlueTableCredentials for Query Session Context.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;mediaconnect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds the DescribeSourceMetadata API. This API can be used to
view the stream information of the flow&#39;s source.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;networkmonitor&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
CloudWatch Network Monitor is a new service within CloudWatch that will
help network administrators and operators continuously monitor network
performance metrics such as round-trip-time and packet loss between
their AWS-hosted applications and their on-premises locations.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;omics&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Provides
minor corrections and an updated description of APIs.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;secretsmanager&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update endpoint rules and examples.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;endpoint-rules&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update endpoint-rules client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.6&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;enhancement:AWSCRT: [&lt;code&gt;botocore&lt;/code&gt;] Update awscrt version to
0.19.19&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;amp&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
updates Amazon Managed Service for Prometheus APIs to support customer
managed KMS keys.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;appintegrations&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] The
Amazon AppIntegrations service adds DeleteApplication API for deleting
applications, and updates APIs to support third party applications
reacting to workspace events and make data requests to Amazon Connect
for agent and contact events.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;bedrock-agent&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release introduces Amazon Aurora as a vector store on Knowledge Bases
for Amazon Bedrock&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;codecommit&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] AWS
CodeCommit now supports customer managed keys from AWS Key Management
Service. UpdateRepositoryEncryptionKey is added for updating the key
configuration. CreateRepository, GetRepository, BatchGetRepositories are
updated with new input or output parameters.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;connect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adds APIs
to manage User Proficiencies and Predefined Attributes. Enhances
StartOutboundVoiceContact API input. Introduces SearchContacts API.
Enhances DescribeContact API. Adds an API to update Routing Attributes
in QueuePriority and QueueTimeAdjustmentSeconds.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;medialive&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] MediaLive
now supports the ability to configure the audio that an AWS Elemental
Link UHD device produces, when the device is configured as the source
for a flow in AWS Elemental MediaConnect.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;neptune-graph&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adds
Waiters for successful creation and deletion of Graph, Graph Snapshot,
Import Task and Private Endpoints for Neptune Analytics&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;rds-data&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds support for using RDS Data API with Aurora PostgreSQL
Serverless v2 and provisioned DB clusters.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;rds&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds support for using RDS Data API with Aurora PostgreSQL Serverless v2
and provisioned DB clusters.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;sagemaker&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Amazon
SageMaker Training now provides model training container access for
debugging purposes. Amazon SageMaker Search now provides the ability to
use visibility conditions to limit resource access to a single domain or
multiple domains.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.5&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;appstream&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release introduces configurable clipboard, allowing admins to specify
the maximum length of text that can be copied by the users from their
device to the remote session and vice-versa.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;eks&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add support for
cluster insights, new EKS capability that surfaces potentially upgrade
impacting issues.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;guardduty&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release 1) introduces a new API: GetOrganizationStatistics , and 2) adds
a new UsageStatisticType TOP_ACCOUNTS_BY_FEATURE for GetUsageStatistics
API&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;managedblockchain-query&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] Adding Confirmation Status and Execution Status
to GetTransaction Response.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;mediatailor&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adds
the ability to configure time shifting on MediaTailor channels using the
TimeShiftConfiguration field&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;route53&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Amazon
Route 53 now supports the Canada West (Calgary) Region (ca-west-1) for
latency records, geoproximity records, and private DNS for Amazon VPCs
in that region.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;endpoint-rules&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update endpoint-rules client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.4&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;appsync&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds additional configurations on GraphQL APIs for limits on
query depth, resolver count, and introspection&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;chime-sdk-meetings&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Add meeting features to specify a maximum camera resolution, a maximum
content sharing resolution, and a maximum number of attendees for a
given meeting.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ec2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Provision
BYOIPv4 address ranges and advertise them by specifying the network
border groups option in Los Angeles, Phoenix and Dallas AWS Local
Zones.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;fsx&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added support
for FSx for OpenZFS on-demand data replication across AWS accounts
and/or regions.Added the IncludeShared attribute for
DescribeSnapshots.Added the CopyStrategy attribute for
OpenZFSVolumeConfiguration.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;marketplace-catalog&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
AWS Marketplace now supports a new API, BatchDescribeEntities, which
returns metadata and content for multiple entities.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;rds&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] RDS - The
release adds two new APIs: DescribeDBRecommendations and
ModifyDBRecommendation&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/b203489453a3905f2b1f0eb07dade72b05aa70c5&#34;&gt;&lt;code&gt;b203489&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.7&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/f2b80de562c6782d0fd0797a844ad849ff54b745&#34;&gt;&lt;code&gt;f2b80de&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.7&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/e46b6114f7aa563d1738e21425a246aef5d214b9&#34;&gt;&lt;code&gt;e46b611&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/e1632bcb1cad4fdb3856d1579f5ffa50b3d146c0&#34;&gt;&lt;code&gt;e1632bc&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.6&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/603daf7323f8d4a6e3eaa4d3f341d1e40378dd62&#34;&gt;&lt;code&gt;603daf7&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.6&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/97a019785f2c95968c18ddc6b5f41c7aa784efc0&#34;&gt;&lt;code&gt;97a0197&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.6&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/b7502b1ead77062f6e76b304672cc01bbf0f7581&#34;&gt;&lt;code&gt;b7502b1&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/3d6e1394e46180fe704c19884263e81f9f70db80&#34;&gt;&lt;code&gt;3d6e139&lt;/code&gt;&lt;/a&gt;
Up minimum version of CRT required to support s3express (&lt;a
href=&#34;https://redirect.github.com/boto/boto3/issues/3979&#34;&gt;#3979&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/26e4bbbb5e334a35ad4875de70b8c700c5013787&#34;&gt;&lt;code&gt;26e4bbb&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.5&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/fdb007638a8a0a208cf42a3b09e9f88699c8e396&#34;&gt;&lt;code&gt;fdb0076&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.5&#39; into develop&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.34.3...1.34.7&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.34.3&amp;new-version=1.34.7)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`52ab1b1`](https://github.com/conijnio/aws-iam-login/commit/52ab1b19972e9e9783397a3193708e7061f8fd8a))

* chore(deps-dev): Bump mypy from 1.7.1 to 1.8.0 (#151)

Bumps [mypy](https://github.com/python/mypy) from 1.7.1 to 1.8.0.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/python/mypy/blob/master/CHANGELOG.md&#34;&gt;mypy&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;Mypy Release Notes&lt;/h1&gt;
&lt;h2&gt;Next release&lt;/h2&gt;
&lt;h2&gt;Mypy 1.8&lt;/h2&gt;
&lt;p&gt;We’ve just uploaded mypy 1.8 to the Python Package Index (&lt;a
href=&#34;https://pypi.org/project/mypy/&#34;&gt;PyPI&lt;/a&gt;). Mypy is a static type
checker for Python. This release includes new features, performance
improvements and bug fixes. You can install it as follows:&lt;/p&gt;
&lt;pre&gt;&lt;code&gt;python3 -m pip install -U mypy
&lt;/code&gt;&lt;/pre&gt;
&lt;p&gt;You can read the full documentation for this release on &lt;a
href=&#34;http://mypy.readthedocs.io&#34;&gt;Read the Docs&lt;/a&gt;.&lt;/p&gt;
&lt;h4&gt;Type-checking Improvements&lt;/h4&gt;
&lt;ul&gt;
&lt;li&gt;Do not intersect types in isinstance checks if at least one is final
(Christoph Tyralla, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16330&#34;&gt;16330&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Detect that &lt;code&gt;@final&lt;/code&gt; class without &lt;code&gt;__bool__&lt;/code&gt;
cannot have falsey instances (Ilya Priven, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16566&#34;&gt;16566&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Do not allow &lt;code&gt;TypedDict&lt;/code&gt; classes with extra keywords
(Nikita Sobolev, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16438&#34;&gt;16438&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Do not allow class-level keywords for &lt;code&gt;NamedTuple&lt;/code&gt;
(Nikita Sobolev, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16526&#34;&gt;16526&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Make imprecise constraints handling more robust (Ivan Levkivskyi, PR
&lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16502&#34;&gt;16502&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix strict-optional in extending generic TypedDict (Ivan Levkivskyi,
PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16398&#34;&gt;16398&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Allow type ignores of PEP 695 constructs (Shantanu, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16608&#34;&gt;16608&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Enable &lt;code&gt;type_check_only&lt;/code&gt; support for
&lt;code&gt;TypedDict&lt;/code&gt; and &lt;code&gt;NamedTuple&lt;/code&gt; (Nikita Sobolev, PR
&lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16469&#34;&gt;16469&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h4&gt;Performance Improvements&lt;/h4&gt;
&lt;ul&gt;
&lt;li&gt;Add fast path to analyzing special form assignments (Jukka
Lehtosalo, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16561&#34;&gt;16561&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h4&gt;Improvements to Error Reporting&lt;/h4&gt;
&lt;ul&gt;
&lt;li&gt;Don&#39;t show documentation links for plugin error codes (Ivan
Levkivskyi, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16383&#34;&gt;16383&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Improve error messages for &lt;code&gt;super&lt;/code&gt; checks and add more
tests (Nikita Sobolev, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16393&#34;&gt;16393&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Add error code for mutable covariant override (Ivan Levkivskyi, PR
&lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16399&#34;&gt;16399&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h4&gt;Stubgen Improvements&lt;/h4&gt;
&lt;ul&gt;
&lt;li&gt;Preserve simple defaults in function signatures (Ali Hamdan, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/15355&#34;&gt;15355&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Include &lt;code&gt;__all__&lt;/code&gt; in output (Jelle Zijlstra, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16356&#34;&gt;16356&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix stubgen regressions with pybind11 and mypy 1.7 (Chad Dombrova,
PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16504&#34;&gt;16504&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h4&gt;Stubtest Improvements&lt;/h4&gt;
&lt;ul&gt;
&lt;li&gt;Improve handling of unrepresentable defaults (Jelle Zijlstra, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16433&#34;&gt;16433&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Print more helpful errors if a function is missing from stub (Alex
Waygood, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16517&#34;&gt;16517&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Support &lt;code&gt;@type_check_only&lt;/code&gt; decorator (Nikita Sobolev, PR
&lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16422&#34;&gt;16422&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Warn about missing &lt;code&gt;__del__&lt;/code&gt; (Shantanu, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16456&#34;&gt;16456&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crashes with some uses of &lt;code&gt;final&lt;/code&gt; and
&lt;code&gt;deprecated&lt;/code&gt; (Shantanu, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16457&#34;&gt;16457&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h4&gt;Fixes to Crashes&lt;/h4&gt;
&lt;ul&gt;
&lt;li&gt;Fix crash with type alias to &lt;code&gt;Callable[[Unpack[Tuple[Any,
...]]], Any]&lt;/code&gt; (Alex Waygood, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16541&#34;&gt;16541&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash on TypeGuard in &lt;code&gt;__call__&lt;/code&gt; (Ivan Levkivskyi, PR
&lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16516&#34;&gt;16516&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash on invalid enum in method (Ivan Levkivskyi, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16511&#34;&gt;16511&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash on unimported Any in TypedDict (Ivan Levkivskyi, PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16510&#34;&gt;16510&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h4&gt;Documentation Updates&lt;/h4&gt;
&lt;ul&gt;
&lt;li&gt;Update soft-error-limit default value to -1 (Sveinung Gundersen, PR
&lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16542&#34;&gt;16542&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/3b467509ee29b8f274c035d78a1c241a781eb311&#34;&gt;&lt;code&gt;3b46750&lt;/code&gt;&lt;/a&gt;
remove +dev suffix from version&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/c9bc833bc8a64e3517a6843bbf982a37ee54f893&#34;&gt;&lt;code&gt;c9bc833&lt;/code&gt;&lt;/a&gt;
Fix tests broken by hatchling (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16655&#34;&gt;#16655&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/60d30e36c49a2753de2d71f7dd50f5143bafd307&#34;&gt;&lt;code&gt;60d30e3&lt;/code&gt;&lt;/a&gt;
Fix crash with type alias to &lt;code&gt;Callable[[Unpack[Tuple[Any, ...]]],
Any]&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16541&#34;&gt;#16541&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/f53f4222bbb12d49612657a48b4f2b77e15402fd&#34;&gt;&lt;code&gt;f53f422&lt;/code&gt;&lt;/a&gt;
Allow type ignores of PEP 695 constructs (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16608&#34;&gt;#16608&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/7c33e7c03444ae748b82163e7b4e1666dfaf94c7&#34;&gt;&lt;code&gt;7c33e7c&lt;/code&gt;&lt;/a&gt;
&lt;a href=&#34;https://github.com/final&#34;&gt;&lt;code&gt;@​final&lt;/code&gt;&lt;/a&gt; class
without &lt;strong&gt;bool&lt;/strong&gt; cannot have falsey instances (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16566&#34;&gt;#16566&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/c224da5c7c414f92ded4b7816d16d5dd4ed32193&#34;&gt;&lt;code&gt;c224da5&lt;/code&gt;&lt;/a&gt;
Do not intersect types in isinstance checks if at least one is final (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16330&#34;&gt;#16330&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/d54cc35a93b1f1bda8f837e0f3ae6f964a1c7feb&#34;&gt;&lt;code&gt;d54cc35&lt;/code&gt;&lt;/a&gt;
Change example in test cases with no stubs available (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16513&#34;&gt;#16513&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/eb1ee973778e3cf719948e1653db9760ea49405d&#34;&gt;&lt;code&gt;eb1ee97&lt;/code&gt;&lt;/a&gt;
Update hashes in &lt;code&gt;sync-typeshed.py&lt;/code&gt; following recent typeshed
sync (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16600&#34;&gt;#16600&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/344298e3a7b1a299092c684c11c28e9f4dc44dd9&#34;&gt;&lt;code&gt;344298e&lt;/code&gt;&lt;/a&gt;
Revert use of &lt;code&gt;ParamSpec&lt;/code&gt; for
&lt;code&gt;functools.wraps&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/3e5d813372e4fc1899319f31425bfc11c27fddb3&#34;&gt;&lt;code&gt;3e5d813&lt;/code&gt;&lt;/a&gt;
Revert typeshed ctypes change&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/python/mypy/compare/v1.7.1...v1.8.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=mypy&amp;package-manager=pip&amp;previous-version=1.7.1&amp;new-version=1.8.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`1f180d6`](https://github.com/conijnio/aws-iam-login/commit/1f180d6cad0dcf5b8e4734a470684257395ed4c2))

* chore(deps-dev): Bump black from 23.12.0 to 23.12.1 (#150)

Bumps [black](https://github.com/psf/black) from 23.12.0 to 23.12.1.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/releases&#34;&gt;black&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.12.1&lt;/h2&gt;
&lt;p&gt;Fixed a bug that included dependencies from the d extra by default
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4108&#34;&gt;#4108&lt;/a&gt;)&lt;/p&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/blob/main/CHANGES.md&#34;&gt;black&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.12.1&lt;/h2&gt;
&lt;h3&gt;Packaging&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fixed a bug that included dependencies from the &lt;code&gt;d&lt;/code&gt; extra
by default (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4108&#34;&gt;#4108&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/ec91a2be3c44d88e1a3960a4937ad6ed3b63464e&#34;&gt;&lt;code&gt;ec91a2b&lt;/code&gt;&lt;/a&gt;
Prepare release 23.12.1 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4124&#34;&gt;#4124&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/8fec1c30855890cc9cfce5ae6d633a1c1a21d724&#34;&gt;&lt;code&gt;8fec1c3&lt;/code&gt;&lt;/a&gt;
Adds paren to deps for hidden extra constraint (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4108&#34;&gt;#4108&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/35ce37ded7bd8fdd3950af19e7c11f311ee7b8d8&#34;&gt;&lt;code&gt;35ce37d&lt;/code&gt;&lt;/a&gt;
Add new changelog template&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/psf/black/compare/23.12.0...23.12.1&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=black&amp;package-manager=pip&amp;previous-version=23.12.0&amp;new-version=23.12.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`19f0760`](https://github.com/conijnio/aws-iam-login/commit/19f0760f83e4828c0af1e2aeaae27fbbd8178dfb))

* chore(deps): Bump boto3 from 1.33.12 to 1.34.3 (#149)

Bumps [boto3](https://github.com/boto/boto3) from 1.33.12 to 1.34.3.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.34.3&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;cognito-idp&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Amazon
Cognito now supports trigger versions that define the fields in the
request sent to pre token generation Lambda triggers.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;eks&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add support for
EKS Cluster Access Management.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;quicksight&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] A
docs-only release to add missing entities to the API reference.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;route53resolver&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add
DOH protocols in resolver endpoints.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.2&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;cloud9&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Updated
Cloud9 API documentation for AL2023 release&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;connect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adds
relatedContactId field to StartOutboundVoiceContact API input.
Introduces PauseContact API and ResumeContact API for Task contacts.
Adds pause duration, number of pauses, timestamps for last paused and
resumed events to DescribeContact API response. Adds new Rule type and
new Rule action.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;connectcases&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Increase number of fields that can be included in CaseEventIncludedData
from 50 to 200&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;kms&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Documentation
updates for AWS Key Management Service&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;rds&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Updates Amazon
RDS documentation by adding code examples&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;sagemaker&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release 1) introduces a new API: DeleteCompilationJob , and 2) adds
InfraCheckConfig for Create/Describe training job API&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.1&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;appstream&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release includes support for images of Windows Server 2022
platform.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;b2bi&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Documentation
updates for AWS B2B Data Interchange&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;billingconductor&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Billing Conductor is releasing a new API, GetBillingGroupCostReport,
which provides the ability to retrieve/view the Billing Group Cost
Report broken down by attributes for a specific billing group.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;connect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds support for more granular billing using tags (key:value
pairs)&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;controltower&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Documentation updates for AWS Control Tower.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;firehose&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release, 1) adds configurable buffering hints for the Splunk
destination, and 2) reduces the minimum configurable buffering interval
for supported destinations&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;gamelift&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Amazon
GameLift adds the ability to add and update the game properties of
active game sessions.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;iot&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds the ability to self-manage certificate signing in AWS IoT Core
fleet provisioning using the new certificate provider resource.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;neptune-graph&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
is the initial SDK release for Amazon Neptune Analytics&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;opensearch&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Updating
documentation for Amazon OpenSearch Service support for new zero-ETL
integration with Amazon S3.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;quicksight&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update
Dashboard Links support; SingleAxisOptions support; Scatterplot Query
limit support.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;workspaces&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Updated
note to ensure customers understand running modes.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;endpoint-rules&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update endpoint-rules client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.34.0&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;feature:Python: End of support for Python 3.7&lt;/li&gt;
&lt;li&gt;feature:Python: [&lt;code&gt;botocore&lt;/code&gt;] End of support for Python
3.7&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;drs&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adding
AgentVersion to SourceServer and RecoveryInstance structures&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.33.13&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;imagebuilder&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds the Image Workflows feature to give more flexibility and
control over the image building and testing process.&lt;/li&gt;
&lt;/ul&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/0a92ebc12ddac3e6ec29c4a8ab2830b3a3d326b6&#34;&gt;&lt;code&gt;0a92ebc&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.3&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/75265ef7d51c29c953e7000efdd25dc2ff5b7ba6&#34;&gt;&lt;code&gt;75265ef&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.3&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/76054b3bb190a9f95c18d99fdc3362b730a9f347&#34;&gt;&lt;code&gt;76054b3&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/227851f4d62cd3e9dd3f13a85badef021d02cd27&#34;&gt;&lt;code&gt;227851f&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.2&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/26526fff0064407ef4e08dafe009f28aadc7993e&#34;&gt;&lt;code&gt;26526ff&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.2&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/ddbf762b40db99c400e80142d7f5f230c0fa7895&#34;&gt;&lt;code&gt;ddbf762&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.2&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/d0800a544aaf7d43c1e47243e16a2972eccf1d83&#34;&gt;&lt;code&gt;d0800a5&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/35fb92b3a97713c2aa83683c2440d2df3522ea33&#34;&gt;&lt;code&gt;35fb92b&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.1&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/59b53f94d5992a1d252b2ba15d3c8283f94f047c&#34;&gt;&lt;code&gt;59b53f9&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.34.1&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/8a1872749d15c7d3fda0b862058a9ba2af88c71b&#34;&gt;&lt;code&gt;8a18727&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.34.1&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.33.12...1.34.3&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.33.12&amp;new-version=1.34.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`dc42daa`](https://github.com/conijnio/aws-iam-login/commit/dc42daa9e72e602d260449453d7dd23f07c1fe19))

* chore(deps-dev): Bump black from 23.11.0 to 23.12.0 (#148)

Bumps [black](https://github.com/psf/black) from 23.11.0 to 23.12.0.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/releases&#34;&gt;black&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.12.0&lt;/h2&gt;
&lt;h3&gt;Highlights&lt;/h3&gt;
&lt;p&gt;It&#39;s almost 2024, which means it&#39;s time for a new edition of
&lt;em&gt;Black&lt;/em&gt;&#39;s stable style!
Together with this release, we&#39;ll put out an alpha release 24.1a1
showcasing the draft
2024 stable style, which we&#39;ll finalize in the January release. Please
try it out and
&lt;a href=&#34;https://redirect.github.com/psf/black/issues/4042&#34;&gt;share your
feedback&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;This release (23.12.0) will still produce the 2023 style. Most but
not all of the
changes in &lt;code&gt;--preview&lt;/code&gt; mode will be in the 2024 stable
style.&lt;/p&gt;
&lt;h3&gt;Stable style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix bug where &lt;code&gt;# fmt: off&lt;/code&gt; automatically dedents when
used with the &lt;code&gt;--line-ranges&lt;/code&gt;
option, even when it is not within the specified line range. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4084&#34;&gt;#4084&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix feature detection for parenthesized context managers (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4104&#34;&gt;#4104&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Prefer more equal signs before a break when splitting chained
assignments (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4010&#34;&gt;#4010&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Standalone form feed characters at the module level are no longer
removed (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4021&#34;&gt;#4021&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional cases of immediately nested tuples, lists, and
dictionaries are now
indented less (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4012&#34;&gt;#4012&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Allow empty lines at the beginning of all blocks, except immediately
before a
docstring (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4060&#34;&gt;#4060&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash in preview mode when using a short
&lt;code&gt;--line-length&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4086&#34;&gt;#4086&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Keep suites consisting of only an ellipsis on their own lines if
they are not
functions or class definitions (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4066&#34;&gt;#4066&lt;/a&gt;) (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4103&#34;&gt;#4103&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;--line-ranges&lt;/code&gt; now skips &lt;em&gt;Black&lt;/em&gt;&#39;s internal
stability check in &lt;code&gt;--safe&lt;/code&gt; mode. This
avoids a crash on rare inputs that have many unformatted same-content
lines. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4034&#34;&gt;#4034&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Packaging&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Upgrade to mypy 1.7.1 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4049&#34;&gt;#4049&lt;/a&gt;) (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4069&#34;&gt;#4069&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Faster compiled wheels are now available for CPython 3.12 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4070&#34;&gt;#4070&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Enable 3.12 CI (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4035&#34;&gt;#4035&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Build docker images in parallel (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4054&#34;&gt;#4054&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Build docker images with 3.12 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4055&#34;&gt;#4055&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/blob/main/CHANGES.md&#34;&gt;black&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.12.0&lt;/h2&gt;
&lt;h3&gt;Highlights&lt;/h3&gt;
&lt;p&gt;It&#39;s almost 2024, which means it&#39;s time for a new edition of
&lt;em&gt;Black&lt;/em&gt;&#39;s stable style!
Together with this release, we&#39;ll put out an alpha release 24.1a1
showcasing the draft
2024 stable style, which we&#39;ll finalize in the January release. Please
try it out and
&lt;a href=&#34;https://redirect.github.com/psf/black/issues/4042&#34;&gt;share your
feedback&lt;/a&gt;.&lt;/p&gt;
&lt;p&gt;This release (23.12.0) will still produce the 2023 style. Most but
not all of the
changes in &lt;code&gt;--preview&lt;/code&gt; mode will be in the 2024 stable
style.&lt;/p&gt;
&lt;h3&gt;Stable style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix bug where &lt;code&gt;# fmt: off&lt;/code&gt; automatically dedents when
used with the &lt;code&gt;--line-ranges&lt;/code&gt;
option, even when it is not within the specified line range. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4084&#34;&gt;#4084&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix feature detection for parenthesized context managers (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4104&#34;&gt;#4104&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Prefer more equal signs before a break when splitting chained
assignments (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4010&#34;&gt;#4010&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Standalone form feed characters at the module level are no longer
removed (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4021&#34;&gt;#4021&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional cases of immediately nested tuples, lists, and
dictionaries are now
indented less (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4012&#34;&gt;#4012&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Allow empty lines at the beginning of all blocks, except immediately
before a
docstring (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4060&#34;&gt;#4060&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash in preview mode when using a short
&lt;code&gt;--line-length&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4086&#34;&gt;#4086&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Keep suites consisting of only an ellipsis on their own lines if
they are not
functions or class definitions (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4066&#34;&gt;#4066&lt;/a&gt;) (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4103&#34;&gt;#4103&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;&lt;code&gt;--line-ranges&lt;/code&gt; now skips &lt;em&gt;Black&lt;/em&gt;&#39;s internal
stability check in &lt;code&gt;--safe&lt;/code&gt; mode. This
avoids a crash on rare inputs that have many unformatted same-content
lines. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4034&#34;&gt;#4034&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Packaging&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Upgrade to mypy 1.7.1 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4049&#34;&gt;#4049&lt;/a&gt;) (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4069&#34;&gt;#4069&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Faster compiled wheels are now available for CPython 3.12 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4070&#34;&gt;#4070&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Enable 3.12 CI (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4035&#34;&gt;#4035&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Build docker images in parallel (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4054&#34;&gt;#4054&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Build docker images with 3.12 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4055&#34;&gt;#4055&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/d9ad09a32b0e0481bb4fef548d35b7a49cc03c5d&#34;&gt;&lt;code&gt;d9ad09a&lt;/code&gt;&lt;/a&gt;
Prepare release 23.12.0 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4105&#34;&gt;#4105&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/ebd543c0ac9b8a5f17636d0a42c425e5f693860e&#34;&gt;&lt;code&gt;ebd543c&lt;/code&gt;&lt;/a&gt;
Fix feature detection for parenthesized context managers (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4104&#34;&gt;#4104&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/eb7661f8ab9bff344835693c7c08789bb195137e&#34;&gt;&lt;code&gt;eb7661f&lt;/code&gt;&lt;/a&gt;
Fix another case where we format dummy implementation for
non-functions/class...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/0c9899956d890a9dc9c3adbc80b478a47846ced9&#34;&gt;&lt;code&gt;0c98999&lt;/code&gt;&lt;/a&gt;
Fix path in test message (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4102&#34;&gt;#4102&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/9aea9768cb60d23f2f4d331e94c4ee07ef1683a5&#34;&gt;&lt;code&gt;9aea976&lt;/code&gt;&lt;/a&gt;
Only use dummy implementation logic for functions and classes (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4066&#34;&gt;#4066&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/67b23d71854c19921cc6092c695d3301ab99229c&#34;&gt;&lt;code&gt;67b23d7&lt;/code&gt;&lt;/a&gt;
Bump actions/setup-python from 4 to 5 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4101&#34;&gt;#4101&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/ce28be2705ab29f184ec4a00aa3d23340630796d&#34;&gt;&lt;code&gt;ce28be2&lt;/code&gt;&lt;/a&gt;
Add dedicated preview feature for East Asian Width (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4097&#34;&gt;#4097&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/61b529b7d15400309379f36104885a1dfcd2d026&#34;&gt;&lt;code&gt;61b529b&lt;/code&gt;&lt;/a&gt;
Allow empty lines at beginning of blocks (again) (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4060&#34;&gt;#4060&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/e7e122e9ff27fc040a6e8ecd92f0e7603c87f92d&#34;&gt;&lt;code&gt;e7e122e&lt;/code&gt;&lt;/a&gt;
docs: Move &lt;code&gt;fmt: off&lt;/code&gt; docs (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4090&#34;&gt;#4090&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/432d9050c3d1e35a36ffc97d4a9e0e0c9e5e4ecc&#34;&gt;&lt;code&gt;432d905&lt;/code&gt;&lt;/a&gt;
docs: Unify option descriptions between &lt;code&gt;--help&lt;/code&gt; and
&lt;code&gt;the_basics.md&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4076&#34;&gt;#4076&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/psf/black/compare/23.11.0...23.12.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=black&amp;package-manager=pip&amp;previous-version=23.11.0&amp;new-version=23.12.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`8082f21`](https://github.com/conijnio/aws-iam-login/commit/8082f21fd44a617f18c382505514f7ea7fb1257b))

* chore(deps): Bump boto3 from 1.33.7 to 1.33.12 (#147)

Bumps [boto3](https://github.com/boto/boto3) from 1.33.7 to 1.33.12.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.33.12&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;neptune&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds a new parameter configuration setting to the Neptune
cluster related APIs that can be leveraged to switch between the
underlying supported storage modes.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;pinpoint&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release includes Amazon Pinpoint API documentation updates pertaining to
campaign message sending rate limits.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;securityhub&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added
new resource detail objects to ASFF, including resources for
AwsDynamoDbTable, AwsEc2ClientVpnEndpoint, AwsMskCluster,
AwsS3AccessPoint, AwsS3Bucket&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;endpoint-rules&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update endpoint-rules client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.33.11&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;cloudwatch&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update
cloudwatch client to latest version&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ec2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] M2 Mac
instances are built on Apple M2 Mac mini computers. I4i instances are
powered by 3rd generation Intel Xeon Scalable processors. C7i compute
optimized, M7i general purpose and R7i memory optimized instances are
powered by custom 4th Generation Intel Xeon Scalable processors.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;finspace&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Releasing
Scaling Group, Dataview, and Volume APIs&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.33.10&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;codedeploy&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds support for two new CodeDeploy features: 1) zonal
deployments for Amazon EC2 in-place deployments, 2) deployments
triggered by Auto Scaling group termination lifecycle hook events.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.33.9&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;backup&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] AWS Backup -
Features: Add VaultType to the output of DescribeRecoveryPoint,
ListRecoveryPointByBackupVault API and add ResourceType to the input of
ListRestoreJobs API&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;comprehend&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Documentation updates for Trust and Safety features.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;connect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Releasing
Tagging Support for Instance Management APIS&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ec2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Releasing the
new cpuManufacturer attribute within the DescribeInstanceTypes API
response which notifies our customers with information on who the
Manufacturer is for the processor attached to the instance, for example:
Intel.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;payment-cryptography&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] AWS Payment Cryptography IPEK feature
release&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.33.8&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;athena&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adding
IdentityCenter enabled request for interactive query&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;cleanroomsml&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Updated service title from cleanroomsml to CleanRoomsML.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;cloudformation&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Documentation update, December 2023&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ec2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adds A10G, T4G,
and H100 as accelerator name options and Habana as an accelerator
manufacturer option for attribute based selection&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/a23fca0d07c03c879fd615f36728c737e25039b3&#34;&gt;&lt;code&gt;a23fca0&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.33.12&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/48d8fc73e29b8d585b6c28ca7dd0df808aa2567c&#34;&gt;&lt;code&gt;48d8fc7&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.33.12&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/c648e3311c4e02f8f7b77a6d4f31663207f4489b&#34;&gt;&lt;code&gt;c648e33&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/0fa37f4f8e0e54db64bc3d23a964b2dc66619a00&#34;&gt;&lt;code&gt;0fa37f4&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/boto/boto3/issues/3969&#34;&gt;#3969&lt;/a&gt; from
boto/dependabot/github_actions/actions/setup-py...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/9534aa0f3afaa953eb0b6062582c1f2ef7a78d26&#34;&gt;&lt;code&gt;9534aa0&lt;/code&gt;&lt;/a&gt;
Bump actions/setup-python from 4.7.0 to 5.0.0&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/339e15a24d38dc0a24cea254707c14aeac4d40b9&#34;&gt;&lt;code&gt;339e15a&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.33.11&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/de188463ed2cccf2c3ead05d55056bb2753aeb2c&#34;&gt;&lt;code&gt;de18846&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.33.11&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/439459f1bdb24c2b59a802fa9e2c1d50e74acb86&#34;&gt;&lt;code&gt;439459f&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.33.11&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/2c627aae3362b5efacda118807caaf31e8ae9f06&#34;&gt;&lt;code&gt;2c627aa&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/504400c307696e393766eecfcaa62729821da54d&#34;&gt;&lt;code&gt;504400c&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.33.10&#39;&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.33.7...1.33.12&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.33.7&amp;new-version=1.33.12)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`7c74e8a`](https://github.com/conijnio/aws-iam-login/commit/7c74e8ade11be46254dc72edae1b392304a9c778))

* chore(deps): Bump boto3 from 1.33.0 to 1.33.7 (#146)

Bumps [boto3](https://github.com/boto/boto3) from 1.33.0 to 1.33.7.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.33.7&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;billingconductor&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
This release adds the ability to specify a linked account of the billing
group for the custom line item resource.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;braket&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
enhances service support to create quantum tasks and hybrid jobs
associated with Braket Direct Reservations.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;cloud9&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds the requirement to include the imageId parameter in the
CreateEnvironmentEC2 API call.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;cloudformation&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Including UPDATE_* states as a success status for CreateStack
waiter.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;finspace&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Release
General Purpose type clusters&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;medialive&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adds
support for custom color correction on channels using 3D LUT files.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;servicecatalog-appregistry&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] Documentation-only updates for Dawn&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;endpoint-rules&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update endpoint-rules client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.33.6&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;qconnect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds the PutFeedback API and allows providing feedback against
the specified assistant for the specified target.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;rbin&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added resource
identifier in the output and updated error handling.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;verifiedpermissions&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Adds description field to PolicyStore API&#39;s and namespaces field to
GetSchema.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.33.5&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;arc-zonal-shift&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
This release adds a new capability, zonal autoshift. You can configure
zonal autoshift so that AWS shifts traffic for a resource away from an
Availability Zone, on your behalf, when AWS determines that there is an
issue that could potentially affect customers in the Availability
Zone.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;glue&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adds
observation and analyzer support to the GetDataQualityResult and
BatchGetDataQualityResult APIs.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;sagemaker&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds support for 1/ Code Editor, based on Code-OSS, Visual
Studio Code Open Source, a new fully managed IDE option in SageMaker
Studio 2/ JupyterLab, a new fully managed JupyterLab IDE experience in
SageMaker Studio&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.33.4&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;bugfix:&lt;code&gt;s3transfer&lt;/code&gt;: Raise floor for
&lt;code&gt;s3transfer&lt;/code&gt; to 0.8.2 to avoid any conflicts with the
awscrt&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;marketplace-agreement&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] The AWS Marketplace Agreement Service provides
an API interface that helps AWS Marketplace sellers manage their
agreements, including listing, filtering, and viewing details about
their agreements.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;marketplace-catalog&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
This release enhances the ListEntities API to support new entity
type-specific strongly typed filters in the request and entity
type-specific strongly typed summaries in the response.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;marketplace-deployment&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] AWS Marketplace Deployment is a new service that
provides essential features that facilitate the deployment of software,
data, and services procured through AWS Marketplace.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;redshift-serverless&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
This release adds the following support for Amazon Redshift Serverless:
1) cross-account cross-VPCs, 2) copying snapshots across Regions, 3)
scheduling snapshot creation, and 4) restoring tables from a recovery
point.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;endpoint-rules&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update endpoint-rules client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.33.3&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;application-autoscaling&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] Amazon SageMaker customers can now use
Application Auto Scaling to automatically scale the number of Inference
Component copies across an endpoint to meet the varying demand of their
workloads.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;cleanrooms&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] AWS
Clean Rooms now provides differential privacy to protect against
user-identification attempts and machine learning modeling to allow two
parties to identify similar users in their data.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;cleanroomsml&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Public
Preview SDK release of AWS Clean Rooms ML APIs&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;opensearch&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Launching Amazon OpenSearch Service support for new zero-ETL integration
with Amazon S3. Customers can now manage their direct query data sources
to Amazon S3 programatically&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;opensearchserverless&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] Amazon OpenSearch Serverless collections support
an additional attribute called standby-replicas. This allows to specify
whether a collection should have redundancy enabled.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;sagemaker-runtime&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update sagemaker-runtime client to latest version&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;sagemaker&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds following support 1/ Improved SDK tooling for model
deployment. 2/ New Inference Component based features to lower inference
costs and latency 3/ SageMaker HyperPod management. 4/ Additional
parameters for FM Fine Tuning in Autopilot&lt;/li&gt;
&lt;/ul&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/0e06fd1ed61fd3551c1007ece9b1285b14556e9b&#34;&gt;&lt;code&gt;0e06fd1&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.33.7&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/9e3d741534a6880c6ad749e6cb07074bfbfdc54d&#34;&gt;&lt;code&gt;9e3d741&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.33.7&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/5a40c63df45851d5fde21f42ba96475e1a5b7f2b&#34;&gt;&lt;code&gt;5a40c63&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/e35ec51fa3963ac2c7c15267382c56708b1834ed&#34;&gt;&lt;code&gt;e35ec51&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.33.6&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/71b905389b4d157c013723284af5a3f61ba6818c&#34;&gt;&lt;code&gt;71b9053&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.33.6&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/51ff38cb0b667e919b816615320ab0f91c28a6cb&#34;&gt;&lt;code&gt;51ff38c&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.33.6&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/ec6bae1753fcc478fb24724b454dc98d5a63dd00&#34;&gt;&lt;code&gt;ec6bae1&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/920bda3cd005ddc49613926aae66d25a93ce0fe8&#34;&gt;&lt;code&gt;920bda3&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.33.5&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/00ecc9bbeb0bc6e0b292f078d12b5dc9e6fe370b&#34;&gt;&lt;code&gt;00ecc9b&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.33.5&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/82b803fc41c3ec053a140fc8b4583204dfc51f53&#34;&gt;&lt;code&gt;82b803f&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.33.5&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.33.0...1.33.7&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.33.0&amp;new-version=1.33.7)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`4f5f8fe`](https://github.com/conijnio/aws-iam-login/commit/4f5f8feb1a4034fe7500dcb23e55014ef6680a98))

* chore(deps-dev): Bump cryptography from 41.0.4 to 41.0.6 (#145)

Bumps [cryptography](https://github.com/pyca/cryptography) from 41.0.4
to 41.0.6.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst&#34;&gt;cryptography&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;p&gt;41.0.6 - 2023-11-27&lt;/p&gt;
&lt;pre&gt;&lt;code&gt;
* Fixed a null-pointer-dereference and segfault that could occur when
loading
certificates from a PKCS#7 bundle. Credit to **pkuzco** for reporting
the
  issue. **CVE-2023-49083**
&lt;p&gt;.. _v41-0-5:&lt;/p&gt;
&lt;p&gt;41.0.5 - 2023-10-24
&lt;/code&gt;&lt;/pre&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Updated Windows, macOS, and Linux wheels to be compiled with OpenSSL
3.1.4.&lt;/li&gt;
&lt;li&gt;Added a function to support an upcoming &lt;code&gt;pyOpenSSL&lt;/code&gt;
release.&lt;/li&gt;
&lt;/ul&gt;
&lt;p&gt;.. _v41-0-4:&lt;/p&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/f09c261ca10a31fe41b1262306db7f8f1da0e48a&#34;&gt;&lt;code&gt;f09c261&lt;/code&gt;&lt;/a&gt;
41.0.6 release (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/9927&#34;&gt;#9927&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/5012bedaef2dc60af3955306774b77ef379116e3&#34;&gt;&lt;code&gt;5012bed&lt;/code&gt;&lt;/a&gt;
bump for 41.0.5 release (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/9766&#34;&gt;#9766&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pyca/cryptography/commit/563b1193997512836603777d31e2ea281b3dc79a&#34;&gt;&lt;code&gt;563b119&lt;/code&gt;&lt;/a&gt;
Added binding needed for pyOpenSSL (&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/9739&#34;&gt;#9739&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/pyca/cryptography/issues/9740&#34;&gt;#9740&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/pyca/cryptography/compare/41.0.4...41.0.6&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=cryptography&amp;package-manager=pip&amp;previous-version=41.0.4&amp;new-version=41.0.6)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)
You can disable automated security fix PRs for this repo from the
[Security Alerts
page](https://github.com/Nr18/aws-iam-login/network/alerts).

&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`a20783c`](https://github.com/conijnio/aws-iam-login/commit/a20783cecc78afeb0d474f48fadcb42061131e22))

* chore(deps): Bump boto3 from 1.29.4 to 1.33.0 (#144)

Bumps [boto3](https://github.com/boto/boto3) from 1.29.4 to 1.33.0.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.33.0&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;enhancement:Versioning: Bump boto3 from 1.29.7 to 1.33.0 to match
Botocore versioning scheme.&lt;/li&gt;
&lt;li&gt;feature:&lt;code&gt;s3&lt;/code&gt;: Boto3 will now opt into using the awscrt on
select EC2 instance types for s3 transfers.&lt;/li&gt;
&lt;li&gt;feature:Versioning: [&lt;code&gt;botocore&lt;/code&gt;] With the release of
Botocore 1.33.0, Boto3 and Botocore will share the same version
number.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;appsync&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This update
enables introspection of Aurora cluster databases using the RDS Data
API&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;b2bi&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This is the
initial SDK release for AWS B2B Data Interchange.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;backup&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] AWS Backup
now supports restore testing, a new feature that allows customers to
automate restore testing and validating their backups. Additionally,
this release adds support for EBS Snapshots Archive tier.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;controltower&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds the following support: 1. The EnableControl API can
configure controls that are configurable. 2. The GetEnabledControl API
shows the configured parameters on an enabled control. 3. The new
UpdateEnabledControl API can change parameters on an enabled
control.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;efs&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update efs
client to latest version&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;fis&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] AWS FIS adds
support for multi-account experiments &amp;amp; empty target resolution.
This release also introduces the CreateTargetAccountConfiguration API
that allows experiments across multiple AWS accounts, and the
ListExperimentResolvedTargets API to list target details.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;glue&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] add
observations support to DQ CodeGen config model + update document for
connectiontypes supported by ConnectorData entities&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;rds&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Updates Amazon
RDS documentation for support for RDS for Db2.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;securityhub&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adds
and updates APIs to support central configuration. This feature allows
the Security Hub delegated administrator to configure Security Hub for
their entire AWS Org across multiple regions from a home Region. With
this release, findings also include account name and application
metadata.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;transcribe&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds support for AWS HealthScribe APIs within Amazon
Transcribe&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;endpoint-rules&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update endpoint-rules client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.29.7&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;enhancement:AWSCRT: [&lt;code&gt;botocore&lt;/code&gt;] Update awscrt version to
0.19.17&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;accessanalyzer&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] IAM
Access Analyzer now continuously monitors IAM roles and users in your
AWS account or organization to generate findings for unused access.
Additionally, IAM Access Analyzer now provides custom policy checks to
validate that IAM policies adhere to your security standards ahead of
deployments.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;amp&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds support for the Amazon Managed Service for Prometheus collector, a
fully managed, agentless Prometheus metrics scraping capability.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;bcm-data-exports&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Users can create, read, update, delete Exports of billing and cost
management data. Users can get details of Export Executions and details
of Tables for exporting. Tagging support is provided for Exports&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;cloudtrail&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
CloudTrail Lake now supports federating event data stores. giving users
the ability to run queries against their event data using Amazon
Athena.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;codestar-connections&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] This release adds support for the CloudFormation
Git sync feature. Git sync enables updating a CloudFormation stack from
a template stored in a Git repository.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;compute-optimizer&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
This release enables AWS Compute Optimizer to analyze and generate
recommendations with customization and discounts preferences.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;config&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Support
Periodic Recording for Configuration Recorder&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;controltower&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add
APIs to create and manage a landing zone.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;cost-optimization-hub&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] This release launches Cost Optimization Hub, a
new AWS Billing and Cost Management feature that helps you consolidate
and prioritize cost optimization recommendations across your AWS
Organizations member accounts and AWS Regions, so that you can get the
most out of your AWS spend.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;detective&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added new
APIs in Detective to support resource investigations&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ecs&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adds a new
&#39;type&#39; property to the Setting structure. Adds a new AccountSetting -
guardDutyActivate for ECS.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;efs&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update efs
client to latest version&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;eks-auth&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds support for EKS Pod Identity feature. EKS Pod Identity
makes it easy for customers to obtain IAM permissions for their
applications running in the EKS clusters.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;eks&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds support for EKS Pod Identity feature. EKS Pod Identity makes it
easy for customers to obtain IAM permissions for the applications
running in their EKS clusters.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;elbv2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update elbv2
client to latest version&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;freetier&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This is
the initial SDK release for the AWS Free Tier GetFreeTierUsage API&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;fsx&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added support
for FSx for ONTAP scale-out file systems and FlexGroup volumes. Added
the HAPairs field and ThroughputCapacityPerHAPair for filesystem. Added
AggregateConfiguration (containing Aggregates and
ConstituentsPerAggregate) and SizeInBytes for volume.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;guardduty&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add
support for Runtime Monitoring for ECS and ECS-EC2.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;iotfleetwise&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] AWS
IoT FleetWise introduces new APIs for vision system data, such as data
collected from cameras, radars, and lidars. You can now model and decode
complex data types.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;lakeformation&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds four new APIs
&amp;quot;DescribeLakeFormationIdentityCenterConfiguration&amp;quot;,
&amp;quot;CreateLakeFormationIdentityCenterConfiguration&amp;quot;,
&amp;quot;DescribeLakeFormationIdentityCenterConfiguration&amp;quot;, and
&amp;quot;DeleteLakeFormationIdentityCenterConfiguration&amp;quot;, and also
updates the corresponding documentation.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;lexv2-models&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update
lexv2-models client to latest version&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;lexv2-runtime&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update lexv2-runtime client to latest version&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;logs&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added APIs to
Create, Update, Get, List and Delete LogAnomalyDetectors and List and
Update Anomalies in Detector. Added LogGroupClass attribute for
LogGroups to classify loggroup as Standard loggroup with all
capabilities or InfrequentAccess loggroup with limited
capabilities.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;managedblockchain&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Add optional NetworkType property to Accessor APIs&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;personalize-events&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
This release enables PutActions and PutActionInteractions&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;personalize-runtime&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Enables metadata in recommendations and next best action
recommendations&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;personalize&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Enables
metadata in recommendations, recommendations with themes, and next best
action recommendations&lt;/li&gt;
&lt;/ul&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/f2a91581f62f454ca0e63517144ef8da10dde841&#34;&gt;&lt;code&gt;f2a9158&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.33.0&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/2b47b716089eedb213ef2e6249940cf5b16ef177&#34;&gt;&lt;code&gt;2b47b71&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.33.0&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/8c316b56746fa552c64bb026a1109aca5092ac8f&#34;&gt;&lt;code&gt;8c316b5&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/9cb7ccc8fa88f5f0232d746dc69f826d09a36f72&#34;&gt;&lt;code&gt;9cb7ccc&lt;/code&gt;&lt;/a&gt;
Add changelog and version bump information&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/675e9b3265838a88d599ddc573b0af60911acc6a&#34;&gt;&lt;code&gt;675e9b3&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/boto/boto3/issues/3946&#34;&gt;#3946&lt;/a&gt; from
nateprewitt/crt_transfer&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/2118dc9728126f008ad87cf3403d7e37f6b944c4&#34;&gt;&lt;code&gt;2118dc9&lt;/code&gt;&lt;/a&gt;
Address feedback&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/ecd17a3a1a1eba28450549190d5bc88e7f388a93&#34;&gt;&lt;code&gt;ecd17a3&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.29.7&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/196a2da7490a1a661a0103b8770bd31e34e147f2&#34;&gt;&lt;code&gt;196a2da&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.29.7&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/75947e3470f7ed72738ec5af0ac77fc871b4fe67&#34;&gt;&lt;code&gt;75947e3&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.29.7&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/45facdeba91437a57f56d8a7f33b53fc7af3b933&#34;&gt;&lt;code&gt;45facde&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.29.4...1.33.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.29.4&amp;new-version=1.33.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`6db9718`](https://github.com/conijnio/aws-iam-login/commit/6db9718dd3bff8e8dfa88af080e7bd1980c6d8fe))

* chore(deps-dev): Bump mypy from 1.7.0 to 1.7.1 (#143)

Bumps [mypy](https://github.com/python/mypy) from 1.7.0 to 1.7.1.
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/6b3c41838d8e7a39242b6fd035535e2d76eabfc6&#34;&gt;&lt;code&gt;6b3c418&lt;/code&gt;&lt;/a&gt;
Update version to 1.7.1 (without +dev)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/c10e17348f2eacbbeae80eb6c10c661c0137d849&#34;&gt;&lt;code&gt;c10e173&lt;/code&gt;&lt;/a&gt;
[mypyc] Fix regression with nested functions (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16484&#34;&gt;#16484&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/e6399d10b0a1cdb104559482fad1b4dc0e2de6ac&#34;&gt;&lt;code&gt;e6399d1&lt;/code&gt;&lt;/a&gt;
Fix polymorphic application for callback protocols (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16514&#34;&gt;#16514&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/661adb756800ecc40fabbe62e9339efd253aff4e&#34;&gt;&lt;code&gt;661adb7&lt;/code&gt;&lt;/a&gt;
Fix crash on strict-equality with recursive types (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16483&#34;&gt;#16483&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/6c8e0cc47c014894ea41621a10f3d1b465322362&#34;&gt;&lt;code&gt;6c8e0cc&lt;/code&gt;&lt;/a&gt;
Ignore position if imprecise arguments are matched by name (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16471&#34;&gt;#16471&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/5c354c41c0fbb74418afcbd30ba822694be28d11&#34;&gt;&lt;code&gt;5c354c4&lt;/code&gt;&lt;/a&gt;
Fix missing meet case exposed by len narrowing (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16470&#34;&gt;#16470&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/88791cabe0521f77b699405154d90f3bb7c6b31b&#34;&gt;&lt;code&gt;88791ca&lt;/code&gt;&lt;/a&gt;
Exclude private attributes from override checks (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16464&#34;&gt;#16464&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/4b5b316beb570bba4c9b7797deb2e6d7df0552d0&#34;&gt;&lt;code&gt;4b5b316&lt;/code&gt;&lt;/a&gt;
Special-case unions in polymorphic inference (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16461&#34;&gt;#16461&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/f862d3ef540c38e7efd2fffd64fc732d6318dfb4&#34;&gt;&lt;code&gt;f862d3e&lt;/code&gt;&lt;/a&gt;
Fix crash on Callable self in &lt;strong&gt;call&lt;/strong&gt; (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16453&#34;&gt;#16453&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/fe79a59e44299a3cc8025aa5084e08773c872a54&#34;&gt;&lt;code&gt;fe79a59&lt;/code&gt;&lt;/a&gt;
Bump version to 1.7.1+dev&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/python/mypy/compare/v1.7.0...v1.7.1&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=mypy&amp;package-manager=pip&amp;previous-version=1.7.0&amp;new-version=1.7.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`15ff329`](https://github.com/conijnio/aws-iam-login/commit/15ff329b6f159b78b5e9d4941ef70ec6b5f57496))

* chore(deps): Bump boto3 from 1.28.85 to 1.29.4 (#142)

Bumps [boto3](https://github.com/boto/boto3) from 1.28.85 to 1.29.4.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.29.4&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;enhancement:IMDS: [&lt;code&gt;botocore&lt;/code&gt;] Adds a config option to
opt out of IMDSv1 fallback&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;codestar-connections&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] This release updates a few CodeStar Connections
related APIs.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;docdb&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Amazon
DocumentDB updates for new cluster storage configuration: Amazon
DocumentDB I/O-Optimized.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ec2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds support for Security group referencing over Transit gateways,
enabling you to simplify Security group management and control of
instance-to-instance traffic across VPCs that are connected by Transit
gateway.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.29.3&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;macie&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] The macie
client has been removed following the deprecation of the service.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;appmesh&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Change the
default value of these fields from 0 to null: MaxConnections,
MaxPendingRequests, MaxRequests, HealthCheckThreshold, PortNumber, and
HealthCheckPolicy -&amp;gt; port. Users are not expected to perceive the
change, except that badRequestException is thrown when required fields
missing configured.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;athena&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adding
SerivicePreProcessing time metric&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;cloud9&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] A minor doc
only update related to changing the date of an API change.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;cloudformation&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds a new flag ImportExistingResources to CreateChangeSet.
Specify this parameter on a CREATE- or UPDATE-type change set to import
existing resources with custom names instead of recreating them.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;codepipeline&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
CodePipeline now supports overriding source revisions to achieve manual
re-deploy of a past revision&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;codestar-connections&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] This release adds support for the CloudFormation
Git sync feature. Git sync enables updating a CloudFormation stack from
a template stored in a Git repository.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;connect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds WISDOM_QUICK_RESPONSES as new IntegrationType of Connect
IntegrationAssociation resource and bug fixes.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;dlm&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added support
for SAP HANA in Amazon Data Lifecycle Manager EBS snapshot lifecycle
policies with pre and post scripts.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ec2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds new features for Amazon VPC IP Address Manager (IPAM) Allowing a
choice between Free and Advanced Tiers, viewing public IP address
insights across regions and in Amazon Cloudwatch, use IPAM to plan your
subnet IPs within a VPC and bring your own autonomous system number to
IPAM.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ecr&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Documentation
and operational updates for Amazon ECR, adding support for pull through
cache rules for upstream registries that require authentication.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;emr&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update emr
client to latest version&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;events&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update
events client to latest version&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;internetmonitor&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Adds new querying capabilities for running data queries on a
monitor&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ivs&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] type &amp;amp;
defaulting refinement to various range properties&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ivschat&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] type &amp;amp;
defaulting refinement to various range properties&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;kinesisvideo&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Docs
only build to bring up-to-date with public docs.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;location&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Remove
default value and allow nullable for request parameters having minimum
value larger than zero.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;medialive&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] MediaLive
has now added support for per-output static image overlay.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;mgn&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Removed invalid
and unnecessary default values.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;osis&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add support
for enabling a persistent buffer when creating or updating an OpenSearch
Ingestion pipeline. Add tags to Pipeline and PipelineSummary response
models.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;pipes&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
TargetParameters now properly supports
BatchJobParameters.ArrayProperties.Size and
BatchJobParameters.RetryStrategy.Attempts being optional, and
EcsTaskParameters.Overrides.EphemeralStorage.SizeInGiB now properly
required when setting EphemeralStorage&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;rds&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds support for option groups and replica enhancements to Amazon RDS
Custom.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;redshift-serverless&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Updated SDK for Amazon Redshift Serverless, which provides the ability
to configure a connection with IAM Identity Center to manage user and
group access to databases.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;redshift&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Updated
SDK for Amazon Redshift, which you can use to configure a connection
with IAM Identity Center to manage access to databases. With these, you
can create a connection through a managed application. You can also
change a managed application, delete it, or get information about an
existing one.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;s3&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Removes all
default 0 values for numbers and false values for booleans&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;sso-admin&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Improves
support for configuring RefreshToken and TokenExchange grants on
applications.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;sso-oidc&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adding
support for &lt;code&gt;sso-oauth:CreateTokenWithIAM&lt;/code&gt;.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;sts&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] API updates for
the AWS Security Token Service&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;trustedadvisor&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] AWS
Trusted Advisor introduces new APIs to enable you to programmatically
access Trusted Advisor best practice checks, recommendations, and
prioritized recommendations. Trusted Advisor APIs enable you to
integrate Trusted Advisor with your operational tools to automate your
workloads.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;verifiedpermissions&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Adding BatchIsAuthorized API which supports multiple authorization
requests against a PolicyStore&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;wisdom&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds QuickResponse as a new Wisdom resource and Wisdom APIs for import,
create, read, search, update and delete QuickResponse resources.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;endpoint-rules&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update endpoint-rules client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.29.2&lt;/h1&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/8a08ce827fabb48447e8e3da020e8cb47c5fd87e&#34;&gt;&lt;code&gt;8a08ce8&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.29.4&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/e7963897e673cf2086c8afa4087790f082f56add&#34;&gt;&lt;code&gt;e796389&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.29.4&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/64c8404b75d2722d4ad17062c176dbd94ae432c4&#34;&gt;&lt;code&gt;64c8404&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/099649924cb3eebb081d09a29d9b2773c80f4a31&#34;&gt;&lt;code&gt;0996499&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.29.3&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/910c00577adbb83a69632d67c63fa67f322284fa&#34;&gt;&lt;code&gt;910c005&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.29.3&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/4a66dc1d7e6d0222ac1ce76c21869f6c4d71dd6f&#34;&gt;&lt;code&gt;4a66dc1&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.29.3&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/d8a36e3c5260fad1fff885f1eb09c3d73807714f&#34;&gt;&lt;code&gt;d8a36e3&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/daac03c9a88eae9e3bdfcc77eae36ae61ce0f9ea&#34;&gt;&lt;code&gt;daac03c&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.29.2&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/8e700efc1aff23002dcd12f7209e4a7a06c13e83&#34;&gt;&lt;code&gt;8e700ef&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.29.2&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/b229d950159280bc4c6328b91d56c203141a0d7d&#34;&gt;&lt;code&gt;b229d95&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.29.2&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.28.85...1.29.4&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.28.85&amp;new-version=1.29.4)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`808d82c`](https://github.com/conijnio/aws-iam-login/commit/808d82ce62f8fae9688572e53f111128bccb682f))

* chore(deps): Bump boto3 from 1.28.83 to 1.28.85 (#141)

Bumps [boto3](https://github.com/boto/boto3) from 1.28.83 to 1.28.85.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.28.85&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;enhancement:AWSCRT: [&lt;code&gt;botocore&lt;/code&gt;] Update awscrt version to
0.19.12&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;dataexchange&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Removed Required trait for DataSet.OriginDetails.ProductId.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;dms&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added new Db2
LUW Target endpoint with related endpoint settings. New executeTimeout
endpoint setting for mysql endpoint. New ReplicationDeprovisionTime
field for serverless describe-replications.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ec2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adds the new
EC2 DescribeInstanceTopology API, which you can use to retrieve the
network topology of your running instances on select platform types to
determine their relative proximity to each other.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ecs&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adds a Client
Token parameter to the ECS RunTask API. The Client Token parameter
allows for idempotent RunTask requests.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;emr&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update emr
client to latest version&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;servicecatalog-appregistry&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] When the customer associates a resource
collection to their application with this new feature, then a new
application tag will be applied to all supported resources that are part
of that collection. This allows customers to more easily find the
application that is associated with those resources.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;endpoint-rules&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update endpoint-rules client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.28.84&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;enhancement:AWSCRT: [&lt;code&gt;botocore&lt;/code&gt;] Update awscrt version to
0.19.10&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;controltower&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] AWS
Control Tower supports tagging for enabled controls. This release
introduces TagResource, UntagResource and ListTagsForResource APIs to
manage tags in existing enabled controls. It updates EnabledControl API
to tag resources at creation time.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;cur&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds support for tagging and customers can now tag report definitions.
Additionally, ReportStatus is now added to report definition to show
when the last delivered time stamp and if it succeeded or not.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ec2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] EC2 adds API
updates to enable ENA Express at instance launch time.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;fms&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adds
optimizeUnassociatedWebACL flag to ManagedServiceData, updates
third-party firewall examples, and other minor documentation
updates.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;marketplace-entitlement&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] Update marketplace-entitlement client to latest
version&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;mediaconvert&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release includes the ability to specify any input source as the primary
input for corresponding follow modes, and allows users to specify fit
and fill behaviors without resizing content.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;rds&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Updates Amazon
RDS documentation for zero-ETL integrations.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;endpoint-rules&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update endpoint-rules client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/64a5986c5b0a8bed6832510a4d44936706bb8b48&#34;&gt;&lt;code&gt;64a5986&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.85&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/19b48e93fde3b590ac085b14b9327fc1230ed87c&#34;&gt;&lt;code&gt;19b48e9&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.28.85&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/00c434345949e46ef79bddb91b0d67f22f7162b1&#34;&gt;&lt;code&gt;00c4343&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/d0da0232235043058e51f199d10adfe37e080c14&#34;&gt;&lt;code&gt;d0da023&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.84&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/8dd177fd5b5cb7606d13c77a17b810515a445fd9&#34;&gt;&lt;code&gt;8dd177f&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.84&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/e43788b52fd303c294e4501a35c5f7f8c8846848&#34;&gt;&lt;code&gt;e43788b&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.28.84&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/2b0e7b38b0aba9e983e934a2f1b8accec11ead54&#34;&gt;&lt;code&gt;2b0e7b3&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/7692e710e7b41add3ebe63e5af8e5953a0e6b984&#34;&gt;&lt;code&gt;7692e71&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.83&#39; into develop&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.28.83...1.28.85&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.28.83&amp;new-version=1.28.85)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`089b124`](https://github.com/conijnio/aws-iam-login/commit/089b1246464d71e73cfa601bc0238d94797f56f2))

* chore(deps-dev): Bump mypy from 1.6.1 to 1.7.0 (#140)

Bumps [mypy](https://github.com/python/mypy) from 1.6.1 to 1.7.0.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/python/mypy/blob/master/CHANGELOG.md&#34;&gt;mypy&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;Mypy Release Notes&lt;/h1&gt;
&lt;h2&gt;Next release&lt;/h2&gt;
&lt;p&gt;Stubgen will now include &lt;code&gt;__all__&lt;/code&gt; in its output if it is
in the input file (PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/16356&#34;&gt;16356&lt;/a&gt;).&lt;/p&gt;
&lt;h2&gt;Mypy 1.7&lt;/h2&gt;
&lt;p&gt;We’ve just uploaded mypy 1.7 to the Python Package Index (&lt;a
href=&#34;https://pypi.org/project/mypy/&#34;&gt;PyPI&lt;/a&gt;). Mypy is a static type
checker for Python. This release includes new features, performance
improvements and bug fixes. You can install it as follows:&lt;/p&gt;
&lt;pre&gt;&lt;code&gt;python3 -m pip install -U mypy
&lt;/code&gt;&lt;/pre&gt;
&lt;p&gt;You can read the full documentation for this release on &lt;a
href=&#34;http://mypy.readthedocs.io&#34;&gt;Read the Docs&lt;/a&gt;.&lt;/p&gt;
&lt;h4&gt;Using TypedDict for &lt;code&gt;**kwargs&lt;/code&gt; Typing&lt;/h4&gt;
&lt;p&gt;Mypy now has support for using &lt;code&gt;Unpack[...]&lt;/code&gt; with a
TypedDict type to annotate &lt;code&gt;**kwargs&lt;/code&gt; arguments enabled by
default. Example:&lt;/p&gt;
&lt;pre lang=&#34;python&#34;&gt;&lt;code&gt;# Or &#39;from typing_extensions import ...&#39;
from typing import TypedDict, Unpack
&lt;p&gt;class Person(TypedDict):
name: str
age: int&lt;/p&gt;
&lt;p&gt;def foo(**kwargs: Unpack[Person]) -&amp;gt; None:
...&lt;/p&gt;
&lt;p&gt;foo(name=&amp;quot;x&amp;quot;, age=1)  # Ok
foo(name=1)  # Error
&lt;/code&gt;&lt;/pre&gt;&lt;/p&gt;
&lt;p&gt;The definition of &lt;code&gt;foo&lt;/code&gt; above is equivalent to the one
below, with keyword-only arguments &lt;code&gt;name&lt;/code&gt; and
&lt;code&gt;age&lt;/code&gt;:&lt;/p&gt;
&lt;pre lang=&#34;python&#34;&gt;&lt;code&gt;def foo(*, name: str, age: int) -&amp;gt; None:
    ...
&lt;/code&gt;&lt;/pre&gt;
&lt;p&gt;Refer to &lt;a href=&#34;https://peps.python.org/pep-0692/&#34;&gt;PEP 692&lt;/a&gt; for
more information. Note that unlike in the current version of the PEP,
mypy always treats signatures with &lt;code&gt;Unpack[SomeTypedDict]&lt;/code&gt; as
equivalent to their expanded forms with explicit keyword arguments, and
there aren&#39;t special type checking rules for TypedDict arguments.&lt;/p&gt;
&lt;p&gt;This was contributed by Ivan Levkivskyi back in 2022 (PR &lt;a
href=&#34;https://redirect.github.com/python/mypy/pull/13471&#34;&gt;13471&lt;/a&gt;).&lt;/p&gt;
&lt;h4&gt;TypeVarTuple Support Enabled (Experimental)&lt;/h4&gt;
&lt;p&gt;Mypy now has support for variadic generics (TypeVarTuple) enabled by
default, as an experimental feature. Refer to &lt;a
href=&#34;https://peps.python.org/pep-0646/&#34;&gt;PEP 646&lt;/a&gt; for the
details.&lt;/p&gt;
&lt;p&gt;TypeVarTuple was implemented by Jared Hance and Ivan Levkivskyi over
several mypy releases, with help from Jukka Lehtosalo.&lt;/p&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/f6b9972329d5d68f6defc92a10cc4c3bc339c27b&#34;&gt;&lt;code&gt;f6b9972&lt;/code&gt;&lt;/a&gt;
Remove +dev from version&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/62bcae2d9bad12c5d3b5dda23dc031e1c7ddf136&#34;&gt;&lt;code&gt;62bcae2&lt;/code&gt;&lt;/a&gt;
Fix handling of tuple type context with unpacks (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16444&#34;&gt;#16444&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/c22294a80b000ea673e407994ac5111644944486&#34;&gt;&lt;code&gt;c22294a&lt;/code&gt;&lt;/a&gt;
Handle TypeVarTupleType when checking overload constraints (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16428&#34;&gt;#16428&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/8813968abb657113df5edfa207db46b0649c9dce&#34;&gt;&lt;code&gt;8813968&lt;/code&gt;&lt;/a&gt;
Fix type narrowing in lambda expressions (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16407&#34;&gt;#16407&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/681e54cfe1642adddc41c4ff11198b8bc955d5af&#34;&gt;&lt;code&gt;681e54c&lt;/code&gt;&lt;/a&gt;
Fix crash on unpack call special-casing (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16381&#34;&gt;#16381&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/f68f46351e30644aefd19900ba1634595adc1d09&#34;&gt;&lt;code&gt;f68f463&lt;/code&gt;&lt;/a&gt;
Fix file reloading in dmypy with --export-types (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16359&#34;&gt;#16359&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/5624f401b3786ebdbe167c27297ed778cce3faa5&#34;&gt;&lt;code&gt;5624f40&lt;/code&gt;&lt;/a&gt;
Fix daemon crash caused by deleted submodule (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16370&#34;&gt;#16370&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/ad0e183b0df7cc3dd94d9e1cd6f5710859beda96&#34;&gt;&lt;code&gt;ad0e183&lt;/code&gt;&lt;/a&gt;
Enable Unpack/TypeVarTuple support (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16354&#34;&gt;#16354&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/b064a5c183b53a84d895bb8e3c36a3a74e24be9c&#34;&gt;&lt;code&gt;b064a5c&lt;/code&gt;&lt;/a&gt;
Fix dmypy inspect on Windows (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16355&#34;&gt;#16355&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/4e30e896486b774cdecaef6d3521a585b8acf8bc&#34;&gt;&lt;code&gt;4e30e89&lt;/code&gt;&lt;/a&gt;
Fix dmypy inspect for namespace packages (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16357&#34;&gt;#16357&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/python/mypy/compare/v1.6.1...v1.7.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=mypy&amp;package-manager=pip&amp;previous-version=1.6.1&amp;new-version=1.7.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`f425de9`](https://github.com/conijnio/aws-iam-login/commit/f425de907911dde90e4430c23eb574416e408bdf))

* chore(deps): Bump boto3 from 1.28.81 to 1.28.83 (#139)

Bumps [boto3](https://github.com/boto/boto3) from 1.28.81 to 1.28.83.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.28.83&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;cloudformation&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Added new ConcurrencyMode feature for AWS CloudFormation StackSets for
faster deployments to target accounts.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;cloudtrail&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] The
Insights in Lake feature lets customers enable CloudTrail Insights on a
source CloudTrail Lake event data store and create a destination event
data store to collect Insights events based on unusual management event
activity in the source event data store.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;comprehend&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds support for toxicity detection and prompt safety
classification.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;connect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds the ability to integrate customer lambda functions with
Connect attachments for scanning and updates the
ListIntegrationAssociations API to support filtering on
IntegrationArn.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ec2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] AWS EBS now
supports Block Public Access for EBS Snapshots. This release introduces
the EnableSnapshotBlockPublicAccess, DisableSnapshotBlockPublicAccess
and GetSnapshotBlockPublicAccessState APIs to manage account-level
public access settings for EBS Snapshots in an AWS Region.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;eks&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adding EKS
Anywhere subscription related operations.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;lambda&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add Custom
runtime on Amazon Linux 2023 (provided.al2023) support to AWS
Lambda.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;logs&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update to
support new APIs for delivery of logs from AWS services.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;omics&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Support UBAM
filetype for Omics Storage and make referenceArn optional&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;endpoint-rules&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update endpoint-rules client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.28.82&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;sqs&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
enables customers to call SQS using AWS JSON-1.0 protocol and bug
fix.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/914bc6669195cb146911ce56db2e845da1a42e9d&#34;&gt;&lt;code&gt;914bc66&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.83&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/2313d8837947d8d30784caced353716c24df58b2&#34;&gt;&lt;code&gt;2313d88&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.28.83&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/a9631bcedc3826826ccf98b341d1d60fc0b08114&#34;&gt;&lt;code&gt;a9631bc&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/a4b5e6371d3ab70187d8fb9c7a5721f4bf64281b&#34;&gt;&lt;code&gt;a4b5e63&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.82&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/117b4bffa8c684cb728f75929f9f437e60367698&#34;&gt;&lt;code&gt;117b4bf&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.82&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/f9dfc2e35091fbbdc068454b233fe93e045f70e5&#34;&gt;&lt;code&gt;f9dfc2e&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.28.82&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/574f9a829f2f07187c3946ad668ba79a8d0d87d8&#34;&gt;&lt;code&gt;574f9a8&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/1cd33223ff66f19132e5f9274e56743d3158b700&#34;&gt;&lt;code&gt;1cd3322&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.81&#39; into develop&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.28.81...1.28.83&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.28.81&amp;new-version=1.28.83)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`892b20b`](https://github.com/conijnio/aws-iam-login/commit/892b20bb15a7df9aa422fcf177cd5a55a3b96eeb))

* chore(deps): Bump boto3 from 1.28.80 to 1.28.81 (#138)

Bumps [boto3](https://github.com/boto/boto3) from 1.28.80 to 1.28.81.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.28.81&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;connect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release clarifies in our public documentation that InstanceId is a
requirement for SearchUsers API requests.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;connectcases&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds the ability to add/view comment authors through
CreateRelatedItem and SearchRelatedItems API. For more information see
&lt;a
href=&#34;https://docs.aws.amazon.com/cases/latest/APIReference/Welcome.html&#34;&gt;https://docs.aws.amazon.com/cases/latest/APIReference/Welcome.html&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;datasync&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
change allows for 0 length access keys and secret keys for object
storage locations. Users can now pass in empty string credentials.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;guardduty&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added API
support for new GuardDuty EKS Audit Log finding types.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;lambda&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add Node 20
(nodejs20.x) support to AWS Lambda.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;lexv2-models&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update
lexv2-models client to latest version&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;omics&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adding Run
UUID and Run Output URI: GetRun and StartRun API response has two new
fields &amp;quot;uuid&amp;quot; and &amp;quot;runOutputUri&amp;quot;.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;rds&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This Amazon RDS
release adds support for patching the OS of an RDS Custom for Oracle DB
instance. You can now upgrade the database or operating system using the
modify-db-instance command.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;redshift-serverless&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Added a new parameter in the workgroup that helps you control your cost
for compute resources. This feature provides a ceiling for RPUs that
Amazon Redshift Serverless can scale up to. When automatic compute
scaling is required, having a higher value for MaxRPU can enhance query
throughput.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;resiliencehub&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] AWS
Resilience Hub enhances Resiliency Score, providing actionable
recommendations to improve application resilience. Amazon Elastic
Kubernetes Service (EKS) operational recommendations have been added to
help improve the resilience posture of your applications.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;sqs&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
enables customers to call SQS using AWS JSON-1.0 protocol.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;endpoint-rules&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update endpoint-rules client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/43789ad7068f29c14c98f8232a2db0b0d604b214&#34;&gt;&lt;code&gt;43789ad&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.81&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/0228ec602ca9052fa7a877125756133c950ad439&#34;&gt;&lt;code&gt;0228ec6&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.28.81&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/7d27f44775937e0867ee7b8580e4e3881eb613a5&#34;&gt;&lt;code&gt;7d27f44&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/285bd0a9b49dab8965c17f301ef31fe4846948f8&#34;&gt;&lt;code&gt;285bd0a&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.80&#39; into develop&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.28.80...1.28.81&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.28.80&amp;new-version=1.28.81)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`57954cc`](https://github.com/conijnio/aws-iam-login/commit/57954cc60a6b2a36cd2c97bab652043e80550c72))

* chore(deps-dev): Bump black from 23.10.1 to 23.11.0 (#137)

Bumps [black](https://github.com/psf/black) from 23.10.1 to 23.11.0.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/releases&#34;&gt;black&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.11.0&lt;/h2&gt;
&lt;h3&gt;Highlights&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Support formatting ranges of lines with the new
&lt;code&gt;--line-ranges&lt;/code&gt; command-line option
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4020&#34;&gt;#4020&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Stable style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix crash on formatting bytes strings that look like docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4003&#34;&gt;#4003&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash when whitespace followed a backslash before newline in a
docstring (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4008&#34;&gt;#4008&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix standalone comments inside complex blocks crashing Black (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4016&#34;&gt;#4016&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash on formatting code like &lt;code&gt;await (a ** b)&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3994&#34;&gt;#3994&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;No longer treat leading f-strings as docstrings. This matches
Python&#39;s behaviour and
fixes a crash (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4019&#34;&gt;#4019&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Multiline dicts and lists that are the sole argument to a function
are now
indented less (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3964&#34;&gt;#3964&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Multiline unpacked dicts and lists as the sole argument to a
function are now also
indented less (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3992&#34;&gt;#3992&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;In f-string debug expressions, quote types that are visible in the
final string
are now preserved (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4005&#34;&gt;#4005&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix a bug where long &lt;code&gt;case&lt;/code&gt; blocks were not split into
multiple lines. Also enable
general trailing comma rules on &lt;code&gt;case&lt;/code&gt; blocks (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4024&#34;&gt;#4024&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Keep requiring two empty lines between module-level docstring and
first function or
class definition (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4028&#34;&gt;#4028&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Add support for single-line format skip with other comments on the
same line (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3959&#34;&gt;#3959&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Consistently apply force exclusion logic before resolving symlinks
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4015&#34;&gt;#4015&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix a bug in the matching of absolute path names in
&lt;code&gt;--include&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3976&#34;&gt;#3976&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Performance&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix mypyc builds on arm64 on macOS (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4017&#34;&gt;#4017&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Black&#39;s pre-commit integration will now run only on git hooks
appropriate for a code
formatter (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3940&#34;&gt;#3940&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/blob/main/CHANGES.md&#34;&gt;black&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.11.0&lt;/h2&gt;
&lt;h3&gt;Highlights&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Support formatting ranges of lines with the new
&lt;code&gt;--line-ranges&lt;/code&gt; command-line option
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4020&#34;&gt;#4020&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Stable style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix crash on formatting bytes strings that look like docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4003&#34;&gt;#4003&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash when whitespace followed a backslash before newline in a
docstring (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4008&#34;&gt;#4008&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix standalone comments inside complex blocks crashing Black (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4016&#34;&gt;#4016&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix crash on formatting code like &lt;code&gt;await (a ** b)&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3994&#34;&gt;#3994&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;No longer treat leading f-strings as docstrings. This matches
Python&#39;s behaviour and
fixes a crash (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4019&#34;&gt;#4019&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Multiline dicts and lists that are the sole argument to a function
are now indented
less (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3964&#34;&gt;#3964&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Multiline unpacked dicts and lists as the sole argument to a
function are now also
indented less (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3992&#34;&gt;#3992&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;In f-string debug expressions, quote types that are visible in the
final string are
now preserved (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4005&#34;&gt;#4005&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix a bug where long &lt;code&gt;case&lt;/code&gt; blocks were not split into
multiple lines. Also enable
general trailing comma rules on &lt;code&gt;case&lt;/code&gt; blocks (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4024&#34;&gt;#4024&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Keep requiring two empty lines between module-level docstring and
first function or
class definition (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4028&#34;&gt;#4028&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Add support for single-line format skip with other comments on the
same line (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3959&#34;&gt;#3959&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Consistently apply force exclusion logic before resolving symlinks
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4015&#34;&gt;#4015&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix a bug in the matching of absolute path names in
&lt;code&gt;--include&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3976&#34;&gt;#3976&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Performance&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix mypyc builds on arm64 on macOS (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4017&#34;&gt;#4017&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Black&#39;s pre-commit integration will now run only on git hooks
appropriate for a code
formatter (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3940&#34;&gt;#3940&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/2a1c67e0b2f81df602ec1f6e7aeb030b9709dc7c&#34;&gt;&lt;code&gt;2a1c67e&lt;/code&gt;&lt;/a&gt;
Prepare release 23.11.0 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4032&#34;&gt;#4032&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/72e7a2e43eef2aa0c83652bb6725eb004a2a69f3&#34;&gt;&lt;code&gt;72e7a2e&lt;/code&gt;&lt;/a&gt;
Remove redundant condition from &lt;code&gt;has_magic_trailing_comma&lt;/code&gt;
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4023&#34;&gt;#4023&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/1a7d9c2f58de1ffcbbe6d133f60f283601ba3f54&#34;&gt;&lt;code&gt;1a7d9c2&lt;/code&gt;&lt;/a&gt;
Preserve visible quote types for f-string debug expressions (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4005&#34;&gt;#4005&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/f4c7be5445c87d9af5eba3d12faea62d2635e3d8&#34;&gt;&lt;code&gt;f4c7be5&lt;/code&gt;&lt;/a&gt;
docs: fix minor typo (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4030&#34;&gt;#4030&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/2e4fac9d87615e904a49e46a9cab2293e0b13126&#34;&gt;&lt;code&gt;2e4fac9&lt;/code&gt;&lt;/a&gt;
Apply force exclude logic before symlink resolution (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4015&#34;&gt;#4015&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/66008fda5dc07f5626e5f5d0dcefc476a9c12ab8&#34;&gt;&lt;code&gt;66008fd&lt;/code&gt;&lt;/a&gt;
[563] Fix standalone comments inside complex blocks crashing Black (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4016&#34;&gt;#4016&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/50ed6221d97b265025abaa66116a7b185f2df5e2&#34;&gt;&lt;code&gt;50ed622&lt;/code&gt;&lt;/a&gt;
Fix long case blocks not split into multiple lines (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4024&#34;&gt;#4024&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/46be1f8e54ac9a7d67723c0fa28c7bec13a0a2bf&#34;&gt;&lt;code&gt;46be1f8&lt;/code&gt;&lt;/a&gt;
Support formatting specified lines (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4020&#34;&gt;#4020&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/ecbd9e8cf71f13068c7e6803a534e00363114c91&#34;&gt;&lt;code&gt;ecbd9e8&lt;/code&gt;&lt;/a&gt;
Fix crash with f-string docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/4019&#34;&gt;#4019&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/e808e61db8c7a8f9c7fd4b2fff2281141f6b2517&#34;&gt;&lt;code&gt;e808e61&lt;/code&gt;&lt;/a&gt;
Preview: Keep requiring two empty lines between module-level docstring
and fi...&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/psf/black/compare/23.10.1...23.11.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=black&amp;package-manager=pip&amp;previous-version=23.10.1&amp;new-version=23.11.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`66f3843`](https://github.com/conijnio/aws-iam-login/commit/66f38438c945fc97807c5e7861673dc4b0d660d8))

* chore(deps): Bump boto3 from 1.28.79 to 1.28.80 (#136)

Bumps [boto3](https://github.com/boto/boto3) from 1.28.79 to 1.28.80.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.28.80&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;dataexchange&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Updated SendDataSetNotificationRequest Comment to be maximum length
4096.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;dlm&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added support
for pre and post scripts in Amazon Data Lifecycle Manager EBS snapshot
lifecycle policies.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;rds&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This Amazon RDS
release adds support for the multi-tenant configuration. In this
configuration, an RDS DB instance can contain multiple tenant databases.
In RDS for Oracle, a tenant database is a pluggable database (PDB).&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;endpoint-rules&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update endpoint-rules client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/894de4bb08fbd42b7556ed71fa214b966e8ed3eb&#34;&gt;&lt;code&gt;894de4b&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.80&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/bb3f218271e6493c45c69c85c385308b7a76fb3c&#34;&gt;&lt;code&gt;bb3f218&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.28.80&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/060bb69f2b6ddb5cdce7c1c43a961c5a07db1065&#34;&gt;&lt;code&gt;060bb69&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/5f075dbba0835541e182130e8bfa98a03c67e674&#34;&gt;&lt;code&gt;5f075db&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.79&#39; into develop&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.28.79...1.28.80&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.28.79&amp;new-version=1.28.80)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`09a455e`](https://github.com/conijnio/aws-iam-login/commit/09a455ed772817f8069377a9e33b57c49b5194cc))

* chore(deps): Bump boto3 from 1.28.78 to 1.28.79 (#135)

Bumps [boto3](https://github.com/boto/boto3) from 1.28.78 to 1.28.79.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.28.79&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;ce&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
extends the GetReservationPurchaseRecommendation API to support
recommendations for Amazon MemoryDB reservations.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;codebuild&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] AWS
CodeBuild now supports AWS Lambda compute.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;connect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added new
API that allows Amazon Connect Outbound Campaigns to create contacts in
Amazon Connect when ingesting your dial requests.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;docdb&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update the
input of CreateDBInstance and ModifyDBInstance to support setting CA
Certificates. Update the output of DescribeDBInstance and
DescribeDBEngineVersions to show current and supported CA
certificates.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;iam&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add partitional
endpoint for iso-e.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;mwaa&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds support for Apache Airflow version 2.7.2. This version release
includes support for deferrable operators and triggers.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;polly&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Amazon Polly
adds new US English voices - Danielle and Gregory. Danielle and Gregory
are available as Neural voices only.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;route53&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add
partitional endpoints for iso-e and iso-f.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;endpoint-rules&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update endpoint-rules client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/18fc144a6d717af85094c8d5031f4e1add413eb6&#34;&gt;&lt;code&gt;18fc144&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.79&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/1175dff92d7ecd96f1f06949d3a368fa51b4a0ab&#34;&gt;&lt;code&gt;1175dff&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.28.79&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/12121c0545c9a2dac0c21ba3b3522ec5cd759549&#34;&gt;&lt;code&gt;12121c0&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/bae6340b70a8fb1e96debcc21fa37a14a41d2805&#34;&gt;&lt;code&gt;bae6340&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.78&#39; into develop&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.28.78...1.28.79&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.28.78&amp;new-version=1.28.79)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`891217d`](https://github.com/conijnio/aws-iam-login/commit/891217d2f777d7b0cdfae8b560c268f401637169))

* chore(deps): Bump boto3 from 1.28.77 to 1.28.78 (#134)

Bumps [boto3](https://github.com/boto/boto3) from 1.28.77 to 1.28.78.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.28.78&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;config&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Updated
ResourceType enum with new resource types onboarded by AWS Config in
October 2023.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;connect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Amazon
Connect Chat introduces Create Persistent Contact Association API,
allowing customers to choose when to resume previous conversations from
previous chats, eliminating the need to repeat themselves and allowing
agents to provide personalized service with access to entire
conversation history.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;iotwireless&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added
LoRaWAN version 1.0.4 support&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;launch-wizard&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] AWS
Launch Wizard is a service that helps reduce the time it takes to deploy
applications to the cloud while providing a guided deployment
experience.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;endpoint-rules&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update endpoint-rules client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/8eaf4062e0366b79799da3c49e0b9b20a1e8ae1c&#34;&gt;&lt;code&gt;8eaf406&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.78&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/d06d3031cbd2ceeb9354c376c4ef2fce9bee5490&#34;&gt;&lt;code&gt;d06d303&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.28.78&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/67e55018c4be597b0801359f867b4a782ddd93ae&#34;&gt;&lt;code&gt;67e5501&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/73c9958e44b8b5f8347f89c514ce067338534157&#34;&gt;&lt;code&gt;73c9958&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/boto/boto3/issues/3919&#34;&gt;#3919&lt;/a&gt; from
kyleknap/fix-changelog&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/b25a193227e810155dae6b0569dec737532a9271&#34;&gt;&lt;code&gt;b25a193&lt;/code&gt;&lt;/a&gt;
Fix changelog&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/b2df09c7f8f0cdf9fa5bd3abc27b28396bad5759&#34;&gt;&lt;code&gt;b2df09c&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.77&#39; into develop&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.28.77...1.28.78&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.28.77&amp;new-version=1.28.78)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`7e0fe97`](https://github.com/conijnio/aws-iam-login/commit/7e0fe9799fdef802afa8695acbf9c32ed654b55d))

* chore(deps): bump boto3 from 1.28.76 to 1.28.77 (#133)

Bumps [boto3](https://github.com/boto/boto3) from 1.28.76 to 1.28.77.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.28.77&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;apprunner&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] AWS App
Runner now supports using dual-stack address type for the public
endpoint of your incoming traffic.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;connect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
GetMetricDataV2 API: Update to include new metrics
PERCENT_NON_TALK_TIME, PERCENT_TALK_TIME, PERCENT_TALK_TIME_AGENT,
PERCENT_TALK_TIME_CUSTOMER&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;gamelift&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Amazon
GameLift adds support for shared credentials, which allows applications
that are deployed on managed EC2 fleets to interact with other AWS
resources.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;glue&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
introduces Google BigQuery Source and Target in AWS Glue
CodeGenConfigurationNode.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;network-firewall&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
This release introduces the stateless rule analyzer, which enables you
to analyze your stateless rules for asymmetric routing.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;quicksight&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release introduces Float Decimal Type as SubType in QuickSight SPICE
datasets and Custom week start and Custom timezone options in Analysis
and Dashboard&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;endpoint-rules&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update endpoint-rules client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/06dcb7103aaf8ec47524205de97203df0eb09bf2&#34;&gt;&lt;code&gt;06dcb71&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.77&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/a4d85d4edc8b024730c825c88e0fa89993210586&#34;&gt;&lt;code&gt;a4d85d4&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.28.77&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/47ac3361b910f4765a4408608ae664889c2fb3be&#34;&gt;&lt;code&gt;47ac336&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/09e173ba6e2659fe9c000736bfaa740bac11ba57&#34;&gt;&lt;code&gt;09e173b&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.76&#39; into develop&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.28.76...1.28.77&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.28.76&amp;new-version=1.28.77)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`b88e502`](https://github.com/conijnio/aws-iam-login/commit/b88e502a64389a36da388db2ec6a54b5f654726b))

* chore(deps): bump boto3 from 1.28.75 to 1.28.76 (#132)

Bumps [boto3](https://github.com/boto/boto3) from 1.28.75 to 1.28.76.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.28.76&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;connect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adds the
BatchGetFlowAssociation API which returns flow associations
(flow-resource) corresponding to the list of resourceArns supplied in
the request. This release also adds IsDefault, LastModifiedRegion and
LastModifiedTime fields to the responses of several Describe and List
APIs.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;globalaccelerator&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Global Accelerator now support accelerators with cross account
endpoints.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;rds&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds support for customized networking resources to Amazon RDS
Custom.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;redshift&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added
support for Multi-AZ deployments for Provisioned RA3 clusters that
provide 99.99% SLA availability.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;sagemaker&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Support
for batch transform input in Model dashboard&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/f51996b26622b9b8870e0aa4dcdee3db9eecf48c&#34;&gt;&lt;code&gt;f51996b&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.76&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/dc8f63558039cb90da37f081aa0e7a2f9d716e68&#34;&gt;&lt;code&gt;dc8f635&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.28.76&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/b3e84112a7a5be4cf861f34e77db208fe55881df&#34;&gt;&lt;code&gt;b3e8411&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/7f3762724c79ee42a2d4ab352c97f0dc191ce030&#34;&gt;&lt;code&gt;7f37627&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.75&#39; into develop&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.28.75...1.28.76&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.28.75&amp;new-version=1.28.76)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`46d40ae`](https://github.com/conijnio/aws-iam-login/commit/46d40ae4bb8ecce4c791f1736eea051ab13b99f6))

* chore(deps): bump boto3 from 1.28.74 to 1.28.75 (#131)

Bumps [boto3](https://github.com/boto/boto3) from 1.28.74 to 1.28.75.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.28.75&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;amplify&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add backend
field to CreateBranch and UpdateBranch requests. Add pagination support
for ListApps, ListDomainAssociations, ListBranches, and ListJobs&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;application-insights&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] Automate attaching managed policies&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ec2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Capacity Blocks
for ML are a new EC2 purchasing option for reserving GPU instances on a
future date to support short duration machine learning (ML) workloads.
Capacity Blocks automatically place instances close together inside
Amazon EC2 UltraClusters for low-latency, high-throughput
networking.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;m2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added name
filter ability for ListDataSets API, added ForceUpdate for Updating
environment and BatchJob submission using S3BatchJobIdentifier&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;neptunedata&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Minor
change to not retry CancelledByUserException&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;translate&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added
support for Brevity translation settings feature.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/eb31d7e289da5f24875c5feb6262e485ea5001c6&#34;&gt;&lt;code&gt;eb31d7e&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.75&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/71c0e8c95db5628fde1fd1d18feaa5fd50e9b8b1&#34;&gt;&lt;code&gt;71c0e8c&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.28.75&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/e4d95887f5e3ddecdeb78665ba0e11c75a8ef9eb&#34;&gt;&lt;code&gt;e4d9588&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/373f07fe11e96fd9eb08144c37b565934ffb2d83&#34;&gt;&lt;code&gt;373f07f&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.74&#39; into develop&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.28.74...1.28.75&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.28.74&amp;new-version=1.28.75)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`9434886`](https://github.com/conijnio/aws-iam-login/commit/9434886684a681ff2d5bbe8d77a23eb3d720906c))

* chore(deps): bump boto3 from 1.28.73 to 1.28.74 (#130)

Bumps [boto3](https://github.com/boto/boto3) from 1.28.73 to 1.28.74.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.28.74&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;connect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds InstanceId field for phone number APIs.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;dataexchange&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] We
added a new API action: SendDataSetNotification.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;datasync&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Platform
version changes to support AL1 deprecation initiative.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;finspace&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Introducing new API UpdateKxClusterCodeConfiguration, introducing new
cache types for clusters and introducing new deployment modes for
updating clusters.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;mediapackagev2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
feature allows customers to create a combination of manifest filtering,
startover and time delay configuration that applies to all egress
requests by default.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;rds&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
launches the CreateIntegration, DeleteIntegration, and
DescribeIntegrations APIs to manage zero-ETL Integrations.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;redshift-serverless&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Added support for custom domain names for Amazon Redshift Serverless
workgroups. This feature enables customers to create a custom domain
name and use ACM to generate fully secure connections to it.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;resiliencehub&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Introduced the ability to filter applications by their last assessment
date and time and have included metrics for the application&#39;s estimated
workload Recovery Time Objective (RTO) and estimated workload Recovery
Point Objective (RPO).&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;s3outposts&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Updated
ListOutpostsWithS3 API response to include S3OutpostArn for use with AWS
RAM.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;wisdom&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
added necessary API documents on creating a Wisdom knowledge base to
integrate with S3.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/e76683b2651e75c5edd1934e02ec27a65939257a&#34;&gt;&lt;code&gt;e76683b&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.74&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/740f4226076bfdc19b146a6c080c53699bdd395a&#34;&gt;&lt;code&gt;740f422&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.28.74&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/1c43d59ddefaf97cada35ca1a67fd9fa3f72387e&#34;&gt;&lt;code&gt;1c43d59&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/3d48fef790ea6c3301280d8ba3d455b487f2fc6c&#34;&gt;&lt;code&gt;3d48fef&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.73&#39; into develop&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.28.73...1.28.74&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.28.73&amp;new-version=1.28.74)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`a3092e7`](https://github.com/conijnio/aws-iam-login/commit/a3092e70562b81c405bbb5c383f9615c7619e852))

* chore(deps): bump boto3 from 1.28.72 to 1.28.73 (#129)

Bumps [boto3](https://github.com/boto/boto3) from 1.28.72 to 1.28.73.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.28.73&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;emr&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update emr
client to latest version&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;neptune&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update
TdeCredentialPassword type to SensitiveString&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;pinpoint&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Updated
documentation to describe the case insensitivity for EndpointIds.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;redshift&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] added
support to create a dual stack cluster&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;wafv2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Updates the
descriptions for the calls that manage web ACL associations, to provide
information for customer-managed IAM policies.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/4d65c8bb612e932b748ca3ae185524b10765509b&#34;&gt;&lt;code&gt;4d65c8b&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.73&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/c9ba56b1dd1cfb096b3779011f92472346011518&#34;&gt;&lt;code&gt;c9ba56b&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.28.73&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/c24c9aacd7052c3b70ab8e837de93760917fc0bd&#34;&gt;&lt;code&gt;c24c9aa&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/a90e88c6b61c7bfc73a5ccfc5e6baae6d7eb7a56&#34;&gt;&lt;code&gt;a90e88c&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.72&#39; into develop&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.28.72...1.28.73&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.28.72&amp;new-version=1.28.73)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`56ee1a7`](https://github.com/conijnio/aws-iam-login/commit/56ee1a75f2ffc780b463bb17e29fc8a012729516))

* chore(deps): bump boto3 from 1.28.71 to 1.28.72 (#128)

Bumps [boto3](https://github.com/boto/boto3) from 1.28.71 to 1.28.72.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.28.72&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;appstream&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release introduces multi-session fleets, allowing customers to provision
more than one user session on a single fleet instance.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ec2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Launching
GetSecurityGroupsForVpc API. This API gets security groups that can be
associated by the AWS account making the request with network interfaces
in the specified VPC.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;network-firewall&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Network Firewall now supports inspection of outbound SSL/TLS
traffic.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;opensearch&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] You can
specify ipv4 or dualstack IPAddressType for cluster endpoints. If you
specify IPAddressType as dualstack, the new endpoint will be visible
under the &#39;EndpointV2&#39; parameter and will support IPv4 and IPv6
requests. Whereas, the &#39;Endpoint&#39; will continue to serve IPv4
requests.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;redshift&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add
Redshift APIs GetResourcePolicy, DeleteResourcePolicy, PutResourcePolicy
and DescribeInboundIntegrations for the new Amazon Redshift Zero-ETL
integration feature, which can be used to control data ingress into
Redshift namespace, and view inbound integrations.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;sagemaker&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Amazon
Sagemaker Autopilot now supports Text Generation jobs.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;sns&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Message
Archiving and Replay is now supported in Amazon SNS for FIFO
topics.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ssm-sap&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] AWS Systems
Manager for SAP added support for registration and discovery of SAP ABAP
applications&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;transfer&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] No API
changes from previous release. This release migrated the model to Smithy
keeping all features unchanged.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;endpoint-rules&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update endpoint-rules client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/b017f647686e15d9845175c7fb32e45c0d98bdf8&#34;&gt;&lt;code&gt;b017f64&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.72&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/01951a8d1e838ebe341ae18f316dff9b332e29c9&#34;&gt;&lt;code&gt;01951a8&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.28.72&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/3913b3e8dc8602bfa5e18bace27b7da1014af1cf&#34;&gt;&lt;code&gt;3913b3e&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/4bb0b0f99941fcf59ee9bf8ff9609aeda14dc774&#34;&gt;&lt;code&gt;4bb0b0f&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.71&#39; into develop&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.28.71...1.28.72&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.28.71&amp;new-version=1.28.72)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`db96756`](https://github.com/conijnio/aws-iam-login/commit/db96756f50fdadaac74b8de2a8a597fab1ad2edc))

* chore(deps): bump boto3 from 1.28.70 to 1.28.71 (#127)

Bumps [boto3](https://github.com/boto/boto3) from 1.28.70 to 1.28.71.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.28.71&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;enhancement:Configuration: [&lt;code&gt;botocore&lt;/code&gt;] Adds client
context params support to &lt;code&gt;Config&lt;/code&gt;.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;connectcases&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Increase maximum length of CommentBody to 3000, and increase maximum
length of StringValue to 1500&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;groundstation&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release will allow KMS alias names to be used when creating Mission
Profiles&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;iam&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Updates to
GetAccessKeyLastUsed action to replace NoSuchEntity error with
AccessDeniedException error.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/d8d3d73c572a62cd188c0ab895e29a477c9daa53&#34;&gt;&lt;code&gt;d8d3d73&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.71&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/1c0db71eab61a0c59111ede48e473fe0703fddbf&#34;&gt;&lt;code&gt;1c0db71&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.28.71&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/cca0f1d18b4821ccb154a2c60577ca28efb1a98d&#34;&gt;&lt;code&gt;cca0f1d&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/3665c15c5f8b62a900dbc3ca33bc22b178a94964&#34;&gt;&lt;code&gt;3665c15&lt;/code&gt;&lt;/a&gt;
add client context params to boto3 docs (&lt;a
href=&#34;https://redirect.github.com/boto/boto3/issues/3911&#34;&gt;#3911&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/29b1640f8214967dae7eca91e27d9db262efeec5&#34;&gt;&lt;code&gt;29b1640&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/boto/boto3/issues/3910&#34;&gt;#3910&lt;/a&gt; from
tim-finnigan/minor-grammar-fix&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/1298d61328387f5dd553c029ccdaeaca3432566a&#34;&gt;&lt;code&gt;1298d61&lt;/code&gt;&lt;/a&gt;
Update config guide to include client context params usage (&lt;a
href=&#34;https://redirect.github.com/boto/boto3/issues/3894&#34;&gt;#3894&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/764506a3b45a9efedc5643240f99e953515f5f53&#34;&gt;&lt;code&gt;764506a&lt;/code&gt;&lt;/a&gt;
remove period&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/05bf2f48d9e53fcd4d024f15853e9e97a806b22a&#34;&gt;&lt;code&gt;05bf2f4&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.70&#39; into develop&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.28.70...1.28.71&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.28.70&amp;new-version=1.28.71)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`d70fc64`](https://github.com/conijnio/aws-iam-login/commit/d70fc6464f278e3a94d19f9609e4226f385b3d42))

* chore(deps): bump boto3 from 1.28.69 to 1.28.70 (#126)

Bumps [boto3](https://github.com/boto/boto3) from 1.28.69 to 1.28.70.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.28.70&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;codepipeline&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add
ability to trigger pipelines from git tags, define variables at pipeline
level and new pipeline type V2.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ec2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
updates the documentation for InstanceInterruptionBehavior and
HibernationOptionsRequest to more accurately describe the behavior of
these two parameters when using Spot hibernation.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;eks&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added support
for Cluster Subnet and Security Group mutability.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;iam&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add the
partitional endpoint for IAM in iso-f.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;migrationhub-config&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
This release introduces DeleteHomeRegionControl API that customers can
use to delete the Migration Hub Home Region configuration&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;migrationhubstrategy&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] This release introduces multi-data-source
feature in Migration Hub Strategy Recommendations. This feature now
supports vCenter as a data source to fetch inventory in addition to ADS
and Import from file workflow that is currently supported with MHSR
collector.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;opensearchserverless&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] This release includes the following new APIs:
CreateLifecyclePolicy, UpdateLifecyclePolicy, BatchGetLifecyclePolicy,
DeleteLifecyclePolicy, ListLifecyclePolicies and
BatchGetEffectiveLifecyclePolicy to support the data lifecycle
management feature.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/c3cdbb430c16de2f22d5caaebc6c7779a5625299&#34;&gt;&lt;code&gt;c3cdbb4&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.70&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/89f4232105f2656c29b9eb2076f279332afc2f0b&#34;&gt;&lt;code&gt;89f4232&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.28.70&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/cf8c1068116fad5e334d309b688009b7237e10b0&#34;&gt;&lt;code&gt;cf8c106&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/95a55df2e56c63b2bcfcb1eac18fa0b95dc54c1d&#34;&gt;&lt;code&gt;95a55df&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.69&#39; into develop&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.28.69...1.28.70&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.28.69&amp;new-version=1.28.70)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`2e26e4c`](https://github.com/conijnio/aws-iam-login/commit/2e26e4ce1c5fd777bc73166883b06872a747fd0a))

* chore(deps-dev): bump pytest from 7.4.2 to 7.4.3 (#125)

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.4.2 to
7.4.3.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pytest-dev/pytest/releases&#34;&gt;pytest&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;pytest 7.4.3 (2023-10-24)&lt;/h2&gt;
&lt;h2&gt;Bug Fixes&lt;/h2&gt;
&lt;ul&gt;
&lt;li&gt;
&lt;p&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/10447&#34;&gt;#10447&lt;/a&gt;:
Markers are now considered in the reverse mro order to ensure base class
markers are considered first -- this resolves a regression.&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11239&#34;&gt;#11239&lt;/a&gt;:
Fixed &lt;code&gt;:=&lt;/code&gt; in asserts impacting unrelated test cases.&lt;/p&gt;
&lt;/li&gt;
&lt;li&gt;
&lt;p&gt;&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11439&#34;&gt;#11439&lt;/a&gt;:
Handled an edge case where :data:&lt;code&gt;sys.stderr&lt;/code&gt; might already
be closed when :ref:&lt;code&gt;faulthandler&lt;/code&gt; is tearing down.&lt;/p&gt;
&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/23906106968eb95afbd61adfbc7bbb795fc9aaa9&#34;&gt;&lt;code&gt;2390610&lt;/code&gt;&lt;/a&gt;
Tweak changelog.rst&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/a0714aa0076f38e6fb8c7321e8bb4f5f33d1792d&#34;&gt;&lt;code&gt;a0714aa&lt;/code&gt;&lt;/a&gt;
Prepare release version 7.4.3&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/44ad1c9811d2ebf540e601ea66b9bebf8ea82969&#34;&gt;&lt;code&gt;44ad1c9&lt;/code&gt;&lt;/a&gt;
[7.4.x] fix &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/10447&#34;&gt;#10447&lt;/a&gt;
- consider marks in reverse mro order to give base classes...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/5dc77253d439038ac64c55a5a48692ac3a53db2e&#34;&gt;&lt;code&gt;5dc7725&lt;/code&gt;&lt;/a&gt;
[7.4.x] Ensure logging tests always cleanup after themselves (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11541&#34;&gt;#11541&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/a5178273183ddbda0ef4e4c6aa2b92aab086776b&#34;&gt;&lt;code&gt;a517827&lt;/code&gt;&lt;/a&gt;
[7.4.x] Configure ReadTheDocs to fail on warnings (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11540&#34;&gt;#11540&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/21fe071d797612468fa18dd0ae4d6dbf49846b6d&#34;&gt;&lt;code&gt;21fe071&lt;/code&gt;&lt;/a&gt;
[7.4.x] fix for ValueError raised in faulthandler teardown code (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11455&#34;&gt;#11455&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/f8bb8572fed8627946bfc82819d24b138d587257&#34;&gt;&lt;code&gt;f8bb857&lt;/code&gt;&lt;/a&gt;
Force terminal width when running tests (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11425&#34;&gt;#11425&lt;/a&gt;)
(&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11432&#34;&gt;#11432&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/1944dc06d39404ae9869b544dc2e2b482bf472e2&#34;&gt;&lt;code&gt;1944dc0&lt;/code&gt;&lt;/a&gt;
[7.4.x] Fix --import-mode=importlib when root contains
&lt;code&gt;__init__.py&lt;/code&gt; file (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/1&#34;&gt;#1&lt;/a&gt;...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/946634c84cf074a1ead10bdba56ddf3e5408e95c&#34;&gt;&lt;code&gt;946634c&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11419&#34;&gt;#11419&lt;/a&gt;
from nicoddemus/backport-11414-to-7.4.x&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pytest-dev/pytest/commit/d849a3ed64c6da63a0e3713892a7bfefdd56acaf&#34;&gt;&lt;code&gt;d849a3e&lt;/code&gt;&lt;/a&gt;
[7.4.x] fix: closes &lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11343&#34;&gt;#11343&lt;/a&gt;&#39;s
[attr-defined] type errors (&lt;a
href=&#34;https://redirect.github.com/pytest-dev/pytest/issues/11421&#34;&gt;#11421&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/pytest-dev/pytest/compare/7.4.2...7.4.3&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=pytest&amp;package-manager=pip&amp;previous-version=7.4.2&amp;new-version=7.4.3)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`5f1ef13`](https://github.com/conijnio/aws-iam-login/commit/5f1ef13bc12668489a7c081599178197e9224596))

* chore(deps): bump boto3 from 1.28.68 to 1.28.69 (#124)

Bumps [boto3](https://github.com/boto/boto3) from 1.28.68 to 1.28.69.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.28.69&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;marketplacecommerceanalytics&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] The StartSupportDataExport operation has been
deprecated as part of the Product Support Connection deprecation. As of
December 2022, Product Support Connection is no longer supported.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;networkmanager&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds API support for Tunnel-less Connect (NoEncap Protocol) for
AWS Cloud WAN&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;redshift-serverless&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
This release adds support for customers to see the patch version and
workgroup version in Amazon Redshift Serverless.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;rekognition&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Amazon
Rekognition introduces StartMediaAnalysisJob, GetMediaAnalysisJob, and
ListMediaAnalysisJobs operations to run a bulk analysis of images with a
Detect Moderation model.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/89d9110610dd7568df37cd3d3a73d7c8a87294a9&#34;&gt;&lt;code&gt;89d9110&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.69&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/58a414e6cb0d37d05277911c361ff450b379caf4&#34;&gt;&lt;code&gt;58a414e&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.28.69&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/7cd39c081119987d994c5448407446901b9df8ad&#34;&gt;&lt;code&gt;7cd39c0&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/b0277975adb6efa7acf7483c71be9e5818e0e51e&#34;&gt;&lt;code&gt;b027797&lt;/code&gt;&lt;/a&gt;
Merge pull request &lt;a
href=&#34;https://redirect.github.com/boto/boto3/issues/3909&#34;&gt;#3909&lt;/a&gt; from
boto/dependabot/github_actions/aws-actions/stal...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/aca0c0a742f1ca81269f2d151079a57d7f23e34c&#34;&gt;&lt;code&gt;aca0c0a&lt;/code&gt;&lt;/a&gt;
Bump aws-actions/stale-issue-cleanup&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/d34d2255494a3dedf98f9b92752aa92378a3f73f&#34;&gt;&lt;code&gt;d34d225&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.68&#39; into develop&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.28.68...1.28.69&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.28.68&amp;new-version=1.28.69)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`ded2b4c`](https://github.com/conijnio/aws-iam-login/commit/ded2b4c0d2c09d8e485f24a7ec1679a114006e63))

* chore(deps-dev): bump black from 23.10.0 to 23.10.1 (#123)

Bumps [black](https://github.com/psf/black) from 23.10.0 to 23.10.1.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/releases&#34;&gt;black&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.10.1&lt;/h2&gt;
&lt;h3&gt;Highlights&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Maintanence release to get a fix out for GitHub Action edge case (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3957&#34;&gt;#3957&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix merging implicit multiline strings that have inline comments (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3956&#34;&gt;#3956&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Allow empty first line after block open before a comment or compound
statement (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3967&#34;&gt;#3967&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Packaging&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Change Dockerfile to hatch + compile black (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3965&#34;&gt;#3965&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;The summary output for GitHub workflows is now suppressible using
the &lt;code&gt;summary&lt;/code&gt;
parameter. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3958&#34;&gt;#3958&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix the action failing when Black check doesn&#39;t pass (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3957&#34;&gt;#3957&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Documentation&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;It is known Windows documentation CI is broken
&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3968&#34;&gt;psf/black#3968&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/blob/main/CHANGES.md&#34;&gt;black&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.10.1&lt;/h2&gt;
&lt;h3&gt;Highlights&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Maintanence release to get a fix out for GitHub Action edge case (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3957&#34;&gt;#3957&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix merging implicit multiline strings that have inline comments (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3956&#34;&gt;#3956&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Allow empty first line after block open before a comment or compound
statement (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3967&#34;&gt;#3967&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Packaging&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Change Dockerfile to hatch + compile black (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3965&#34;&gt;#3965&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;The summary output for GitHub workflows is now suppressible using
the &lt;code&gt;summary&lt;/code&gt;
parameter. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3958&#34;&gt;#3958&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix the action failing when Black check doesn&#39;t pass (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3957&#34;&gt;#3957&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Documentation&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;It is known Windows documentation CI is broken
&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3968&#34;&gt;psf/black#3968&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/744d23b34800c06e10272149b70752396e90eeb8&#34;&gt;&lt;code&gt;744d23b&lt;/code&gt;&lt;/a&gt;
Prepare release 23.10.1 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3969&#34;&gt;#3969&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/8de4be516879302afce542ac80a6a43ced807759&#34;&gt;&lt;code&gt;8de4be5&lt;/code&gt;&lt;/a&gt;
Fix CI failing (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3957&#34;&gt;#3957&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/c0adca321dc0d97a704de8ed0353e5b894a6a912&#34;&gt;&lt;code&gt;c0adca3&lt;/code&gt;&lt;/a&gt;
docs: specifies the use of the .git-blame-ignore-revs file (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3961&#34;&gt;#3961&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/a7643fac8d97c15640a2b1a79f68b3dc771aebfb&#34;&gt;&lt;code&gt;a7643fa&lt;/code&gt;&lt;/a&gt;
Add summary parameter to action (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3958&#34;&gt;#3958&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/d291c2338c3c1feee4f3f26985c0964ec1b7eb9f&#34;&gt;&lt;code&gt;d291c23&lt;/code&gt;&lt;/a&gt;
Move Docker image to hatch + compile (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3965&#34;&gt;#3965&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/7f1c578b89b2c256a6ce3b70fc1b970b3ffa3349&#34;&gt;&lt;code&gt;7f1c578&lt;/code&gt;&lt;/a&gt;
Bump peter-evans/create-or-update-comment from 3.0.2 to 3.1.0 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3966&#34;&gt;#3966&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/2db5ab0a7b3b321e4cec70964239ee88087cd810&#34;&gt;&lt;code&gt;2db5ab0&lt;/code&gt;&lt;/a&gt;
Allow empty line after block open before a comment or compound statement
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3967&#34;&gt;#3967&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/0a37888e79059018eef9293a724b14da59d3377a&#34;&gt;&lt;code&gt;0a37888&lt;/code&gt;&lt;/a&gt;
Fix typos in CHANGES.md (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3963&#34;&gt;#3963&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/882d8795c6ff65c02f2657e596391748d1b6b7f5&#34;&gt;&lt;code&gt;882d879&lt;/code&gt;&lt;/a&gt;
Fix merging implicit multiline strings that have inline comments (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3956&#34;&gt;#3956&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/psf/black/compare/23.10.0...23.10.1&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=black&amp;package-manager=pip&amp;previous-version=23.10.0&amp;new-version=23.10.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`4a9f4f2`](https://github.com/conijnio/aws-iam-login/commit/4a9f4f22ed15adf41736630ee2093f2257d141db))

* chore(deps): bump boto3 from 1.28.67 to 1.28.68 (#122)

Bumps [boto3](https://github.com/boto/boto3) from 1.28.67 to 1.28.68.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.28.68&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;appconfig&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update
KmsKeyIdentifier constraints to support AWS KMS multi-Region keys.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;appintegrations&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Updated ScheduleConfig to be an optional input to CreateDataIntegration
to support event driven downloading of files from sources such as Amazon
s3 using Amazon Connect AppIntegrations.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;connect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds support for updating phone number metadata, such as phone
number description.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;discovery&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release introduces three new APIs: StartBatchDeleteConfigurationTask,
DescribeBatchDeleteConfigurationTask, and BatchDeleteAgents.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;medical-imaging&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Updates on documentation links&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ssm&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
introduces a new API: DeleteOpsItem. This allows deletion of an
OpsItem.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/d42b9fe0c76a2dee0b96fd0f0de6b296d20a8c86&#34;&gt;&lt;code&gt;d42b9fe&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.68&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/01fe1303ee6e083dfe6548500e1ed6089e4ad1ba&#34;&gt;&lt;code&gt;01fe130&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.28.68&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/b39e72005b9d496020600a5054b59712545c2aa1&#34;&gt;&lt;code&gt;b39e720&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/41e2804c9958b6d23087727c8ebdd9373a567251&#34;&gt;&lt;code&gt;41e2804&lt;/code&gt;&lt;/a&gt;
update ci to use GA python 3.12 (&lt;a
href=&#34;https://redirect.github.com/boto/boto3/issues/3908&#34;&gt;#3908&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/9b689a49a91ae2c61d8ae0fe33c318ce3ff940ab&#34;&gt;&lt;code&gt;9b689a4&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.67&#39; into develop&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.28.67...1.28.68&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.28.67&amp;new-version=1.28.68)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`ade204b`](https://github.com/conijnio/aws-iam-login/commit/ade204bd529faf4f65f84a4da3f2c5406d58c186))

* chore(deps): bump boto3 from 1.28.66 to 1.28.67 (#121)

Bumps [boto3](https://github.com/boto/boto3) from 1.28.66 to 1.28.67.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.28.67&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;gamesparks&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] The
gamesparks client has been removed following the deprecation of the
service.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ec2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Amazon EC2 C7a
instances, powered by 4th generation AMD EPYC processors, are ideal for
high performance, compute-intensive workloads such as high performance
computing. Amazon EC2 R7i instances are next-generation memory optimized
and powered by custom 4th Generation Intel Xeon Scalable
processors.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;managedblockchain-query&lt;/code&gt;:
[&lt;code&gt;botocore&lt;/code&gt;] This release adds support for Ethereum Sepolia
network&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;neptunedata&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Doc
changes to add IAM action mappings for the data actions.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;omics&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This change
enables customers to retrieve failure reasons with detailed status
messages for their failed runs&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;opensearch&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added
Cluster Administrative options for node restart, opensearch process
restart and opensearch dashboard restart for Multi-AZ without standby
domains&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;quicksight&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds the following: 1) Trino and Starburst Database Connectors
2) Custom total for tables and pivot tables 3) Enable restricted folders
4) Add rolling dates for time equality filters 5) Refine DataPathValue
and introduce DataPathType 6) Add SeriesType to
ReferenceLineDataConfiguration&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;secretsmanager&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Documentation updates for Secrets Manager&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;servicecatalog&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Introduce support for EXTERNAL product and provisioning artifact type in
CreateProduct and CreateProvisioningArtifact APIs.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;verifiedpermissions&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Improving Amazon Verified Permissions Create experience&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;workspaces&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Documentation updates for WorkSpaces&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/e4b2cc5b9443f726fc5d6c81192f6f1ef388597b&#34;&gt;&lt;code&gt;e4b2cc5&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.67&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/ab918b2de48587cbd1e0b203cffa609af8ecf9ba&#34;&gt;&lt;code&gt;ab918b2&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.28.67&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/f76edf1f86fe71a70d851a5ac1e52d95c5c75234&#34;&gt;&lt;code&gt;f76edf1&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/4c34032a4dfe5371bb7ab808c65e3187398d5153&#34;&gt;&lt;code&gt;4c34032&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.66&#39; into develop&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.28.66...1.28.67&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.28.66&amp;new-version=1.28.67)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`97e1fe4`](https://github.com/conijnio/aws-iam-login/commit/97e1fe49bcc81b435f99522cb234bc4aabdc1f92))

* chore(deps): bump boto3 from 1.28.65 to 1.28.66 (#120)

Bumps [boto3](https://github.com/boto/boto3) from 1.28.65 to 1.28.66.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.28.66&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;cloud9&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update to
imageId parameter behavior and dates updated.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;dynamodb&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Updating
descriptions for several APIs.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;kendra&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Changes for
a new feature in Amazon Kendra&#39;s Query API to Collapse/Expand query
results&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;rds&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds support for upgrading the storage file system configuration on the
DB instance using a blue/green deployment or a read replica.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;wisdom&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds an max limit of 25 recommendation ids for
NotifyRecommendationsReceived API.&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/b090311f3d468516fce097ec3ba1075b5602b240&#34;&gt;&lt;code&gt;b090311&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.66&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/614493040d52098c72623172b77f871b4fe05ad7&#34;&gt;&lt;code&gt;6144930&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.28.66&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/4482f639880a2757ffdc1041afabf008dd68bc48&#34;&gt;&lt;code&gt;4482f63&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/574698a7f5b54022c2f3a5ddb2e9fa696263dfa7&#34;&gt;&lt;code&gt;574698a&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.28.65&#39; into develop&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.28.65...1.28.66&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.28.65&amp;new-version=1.28.66)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`c83f7b7`](https://github.com/conijnio/aws-iam-login/commit/c83f7b72b1cd607128b8ca4b10309b38c7a04f79))

* chore(deps-dev): bump black from 23.9.1 to 23.10.0 (#116)

Bumps [black](https://github.com/psf/black) from 23.9.1 to 23.10.0.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/releases&#34;&gt;black&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.10.0&lt;/h2&gt;
&lt;h3&gt;Stable style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix comments getting removed from inside parenthesized strings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3909&#34;&gt;#3909&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix long lines with power operators getting split before the line
length (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3942&#34;&gt;#3942&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Long type hints are now wrapped in parentheses and properly indented
when split across
multiple lines (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3899&#34;&gt;#3899&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Magic trailing commas are now respected in return types. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3916&#34;&gt;#3916&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Require one empty line after module-level docstrings. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3932&#34;&gt;#3932&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Treat raw triple-quoted strings as docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3947&#34;&gt;#3947&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix cache versioning logic when &lt;code&gt;BLACK_CACHE_DIR&lt;/code&gt; is set
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3937&#34;&gt;#3937&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Parser&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix bug where attributes named &lt;code&gt;type&lt;/code&gt; were not acccepted
inside &lt;code&gt;match&lt;/code&gt; statements
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3950&#34;&gt;#3950&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Add support for PEP 695 type aliases containing lambdas and other
unusual expressions
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3949&#34;&gt;#3949&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Output&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Black no longer attempts to provide special errors for attempting to
format Python 2
code (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3933&#34;&gt;#3933&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Black will more consistently print stacktraces on internal errors in
verbose mode
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3938&#34;&gt;#3938&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;The action output displayed in the job summary is now wrapped in
Markdown (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3914&#34;&gt;#3914&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/blob/main/CHANGES.md&#34;&gt;black&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.10.0&lt;/h2&gt;
&lt;h3&gt;Stable style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix comments getting removed from inside parenthesized strings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3909&#34;&gt;#3909&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix long lines with power operators getting split before the line
length (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3942&#34;&gt;#3942&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Long type hints are now wrapped in parentheses and properly indented
when split across
multiple lines (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3899&#34;&gt;#3899&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Magic trailing commas are now respected in return types. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3916&#34;&gt;#3916&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Require one empty line after module-level docstrings. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3932&#34;&gt;#3932&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Treat raw triple-quoted strings as docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3947&#34;&gt;#3947&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Configuration&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix cache versioning logic when &lt;code&gt;BLACK_CACHE_DIR&lt;/code&gt; is set
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3937&#34;&gt;#3937&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Parser&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Fix bug where attributes named &lt;code&gt;type&lt;/code&gt; were not acccepted
inside &lt;code&gt;match&lt;/code&gt; statements
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3950&#34;&gt;#3950&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Add support for PEP 695 type aliases containing lambdas and other
unusual expressions
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3949&#34;&gt;#3949&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Output&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Black no longer attempts to provide special errors for attempting to
format Python 2
code (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3933&#34;&gt;#3933&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Black will more consistently print stacktraces on internal errors in
verbose mode
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3938&#34;&gt;#3938&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;The action output displayed in the job summary is now wrapped in
Markdown (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3914&#34;&gt;#3914&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/9edba85f71d50d12996ef7bda576426362016171&#34;&gt;&lt;code&gt;9edba85&lt;/code&gt;&lt;/a&gt;
Prepare release 23.10.0 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3951&#34;&gt;#3951&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/bb588073ab286a9f1f8d839ab2cebe13011dd22c&#34;&gt;&lt;code&gt;bb58807&lt;/code&gt;&lt;/a&gt;
Fix parser bug where &amp;quot;type&amp;quot; was misinterpreted as a keyword
inside a match (#...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/722735d20ebdc66c0da0e0df7658293455694500&#34;&gt;&lt;code&gt;722735d&lt;/code&gt;&lt;/a&gt;
Fix grammar for type alias support (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3949&#34;&gt;#3949&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/abe57e3d92727f1b26c717fad3978159b987fe79&#34;&gt;&lt;code&gt;abe57e3&lt;/code&gt;&lt;/a&gt;
Treat raw strings like other docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3947&#34;&gt;#3947&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/1648ac51806d092c95cb9bb2e4a5bffda6095bc1&#34;&gt;&lt;code&gt;1648ac5&lt;/code&gt;&lt;/a&gt;
Fix long lines with power operator(s) getting splitted before line
length (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3&#34;&gt;#3&lt;/a&gt;...&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/6f84f652850dca8a1b578581e2fbb2cb95e791cc&#34;&gt;&lt;code&gt;6f84f65&lt;/code&gt;&lt;/a&gt;
Migrate mypy config to pyproject.toml (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3936&#34;&gt;#3936&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/3bb92146f59804a6ead47d5f2d0fdc47daa6b698&#34;&gt;&lt;code&gt;3bb9214&lt;/code&gt;&lt;/a&gt;
CI Test: Deprecating &#39;Healthcheck.all()&#39; from Hypothesis in fuzz.py (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3945&#34;&gt;#3945&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/935f303a0a7b794e722c7df00c906be285884874&#34;&gt;&lt;code&gt;935f303&lt;/code&gt;&lt;/a&gt;
Fix test that was not being run (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3939&#34;&gt;#3939&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/b7717c3f1e73d6b847e2534a2cebbb657b96caf8&#34;&gt;&lt;code&gt;b7717c3&lt;/code&gt;&lt;/a&gt;
Standardise newlines after module-level docstrings (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3932&#34;&gt;#3932&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/7aa37ea0adf864baf3ef3dfbcfaf5ff1ff780250&#34;&gt;&lt;code&gt;7aa37ea&lt;/code&gt;&lt;/a&gt;
Report all stacktraces in verbose mode (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3938&#34;&gt;#3938&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/psf/black/compare/23.9.1...23.10.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=black&amp;package-manager=pip&amp;previous-version=23.9.1&amp;new-version=23.10.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`0f26b37`](https://github.com/conijnio/aws-iam-login/commit/0f26b377c7683fc982915288fae979cb83a7e895))

* chore(deps-dev): bump mypy from 1.6.0 to 1.6.1 (#119)

Bumps [mypy](https://github.com/python/mypy) from 1.6.0 to 1.6.1.
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/9b891fe5a101ecbb818f3f16641ab909f289ba04&#34;&gt;&lt;code&gt;9b891fe&lt;/code&gt;&lt;/a&gt;
Remove +dev from version&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/6b6504eb8a96fa6a9c7b8f034803eb9a0444fe86&#34;&gt;&lt;code&gt;6b6504e&lt;/code&gt;&lt;/a&gt;
Fix crash on ParamSpec unification (for real) (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16259&#34;&gt;#16259&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/eb81e63e9dec4dd4c75b307871d1ef9b3e350838&#34;&gt;&lt;code&gt;eb81e63&lt;/code&gt;&lt;/a&gt;
Fix crash on ParamSpec unification (&lt;a
href=&#34;https://redirect.github.com/python/mypy/issues/16251&#34;&gt;#16251&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/python/mypy/commit/45f7a12e558e4a48446af3b36494dcb4045c1028&#34;&gt;&lt;code&gt;45f7a12&lt;/code&gt;&lt;/a&gt;
Add +dev to version&lt;/li&gt;
&lt;li&gt;See full diff in &lt;a
href=&#34;https://github.com/python/mypy/compare/v1.6.0...v1.6.1&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=mypy&amp;package-manager=pip&amp;previous-version=1.6.0&amp;new-version=1.6.1)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot show &lt;dependency name&gt; ignore conditions` will show all
of the ignore conditions of the specified dependency
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt;

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`0dcc3f9`](https://github.com/conijnio/aws-iam-login/commit/0dcc3f9cf9a831ccf083c98f3d0bd766b15bc174))

* chore: tweak dependabot ([`d703853`](https://github.com/conijnio/aws-iam-login/commit/d703853f547b7f3f5c84676151ab7a59503f1021))

* chore(deps): bump urllib3 from 1.26.17 to 1.26.18 (#118) ([`de992ee`](https://github.com/conijnio/aws-iam-login/commit/de992eedd98c4ed0306cd3b141e6ecb2c2e94f16))

* chore(deps): bump urllib3 from 1.26.17 to 1.26.18

Bumps [urllib3](https://github.com/urllib3/urllib3) from 1.26.17 to 1.26.18.
- [Release notes](https://github.com/urllib3/urllib3/releases)
- [Changelog](https://github.com/urllib3/urllib3/blob/main/CHANGES.rst)
- [Commits](https://github.com/urllib3/urllib3/compare/1.26.17...1.26.18)

---
updated-dependencies:
- dependency-name: urllib3
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`46a1513`](https://github.com/conijnio/aws-iam-login/commit/46a151342d2103a1e74417601dde58c422b6f9c7))

* chore(deps): bump boto3 from 1.28.64 to 1.28.65 (#117) ([`b81bae2`](https://github.com/conijnio/aws-iam-login/commit/b81bae2022949f51d0f1a3cd351eb1eb3e43a67c))

* chore(deps): bump boto3 from 1.28.64 to 1.28.65

Bumps [boto3](https://github.com/boto/boto3) from 1.28.64 to 1.28.65.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.64...1.28.65)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`fe1e83f`](https://github.com/conijnio/aws-iam-login/commit/fe1e83f1ae1c2fc775b3b250e4685ff08b54e5aa))

* chore(deps): bump boto3 from 1.28.63 to 1.28.64 (#115) ([`7ff035b`](https://github.com/conijnio/aws-iam-login/commit/7ff035b8286b195d00c43f486623f6e2a6e646dd))

* chore(deps): bump boto3 from 1.28.63 to 1.28.64

Bumps [boto3](https://github.com/boto/boto3) from 1.28.63 to 1.28.64.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.63...1.28.64)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`6c6465c`](https://github.com/conijnio/aws-iam-login/commit/6c6465ca5cc89750b413c02f414d43c6649f48c1))

* chore(deps): bump boto3 from 1.28.62 to 1.28.63 (#114) ([`f1e0fbb`](https://github.com/conijnio/aws-iam-login/commit/f1e0fbbca0d83051ba36399112faf478c404e2fe))

* chore(deps): bump boto3 from 1.28.62 to 1.28.63

Bumps [boto3](https://github.com/boto/boto3) from 1.28.62 to 1.28.63.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.62...1.28.63)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`399e37f`](https://github.com/conijnio/aws-iam-login/commit/399e37f4cb0d0a5a04c9e0dccd7e5ca92c4e9682))

* chore(deps-dev): bump mypy from 1.5.1 to 1.6.0 (#113) ([`077a79e`](https://github.com/conijnio/aws-iam-login/commit/077a79ef78ec32bd0cfd78ed45d2a86c5050f2db))

* chore(deps-dev): bump mypy from 1.5.1 to 1.6.0

Bumps [mypy](https://github.com/python/mypy) from 1.5.1 to 1.6.0.
- [Commits](https://github.com/python/mypy/compare/v1.5.1...v1.6.0)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`1f9e829`](https://github.com/conijnio/aws-iam-login/commit/1f9e829fdfd9868e28535d1c2ff75abafef4ea02))

* chore(deps): bump boto3 from 1.28.61 to 1.28.62 (#112) ([`e5b9d67`](https://github.com/conijnio/aws-iam-login/commit/e5b9d678b8b9f37efb60b0908819c650bf1478c8))

* chore(deps): bump boto3 from 1.28.61 to 1.28.62

Bumps [boto3](https://github.com/boto/boto3) from 1.28.61 to 1.28.62.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.61...1.28.62)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`b97bd06`](https://github.com/conijnio/aws-iam-login/commit/b97bd0688bbd8306fbc7064b54bae5e758743fa9))

* chore(deps): bump boto3 from 1.28.60 to 1.28.61 (#111) ([`8df1ec6`](https://github.com/conijnio/aws-iam-login/commit/8df1ec60dfcfe5906d9cd24b65c77b537e4e7fe7))

* chore(deps): bump boto3 from 1.28.60 to 1.28.61

Bumps [boto3](https://github.com/boto/boto3) from 1.28.60 to 1.28.61.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.60...1.28.61)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`deaeee0`](https://github.com/conijnio/aws-iam-login/commit/deaeee030bf45bcd34b5974e873306d51e891de6))

* chore(deps): bump boto3 from 1.28.59 to 1.28.60 (#110) ([`927489f`](https://github.com/conijnio/aws-iam-login/commit/927489f36cf0539242a5b1f40ba3cdeade594fec))

* chore(deps): bump boto3 from 1.28.59 to 1.28.60

Bumps [boto3](https://github.com/boto/boto3) from 1.28.59 to 1.28.60.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.59...1.28.60)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`4a05b23`](https://github.com/conijnio/aws-iam-login/commit/4a05b23a92edfa8ed32ef055466f58022ff1beed))

* chore(deps): bump boto3 from 1.28.58 to 1.28.59 (#109) ([`89c2a12`](https://github.com/conijnio/aws-iam-login/commit/89c2a12ff53b54804ce788177f95e403a7ec603e))

* chore(deps): bump boto3 from 1.28.58 to 1.28.59

Bumps [boto3](https://github.com/boto/boto3) from 1.28.58 to 1.28.59.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.58...1.28.59)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`0a16242`](https://github.com/conijnio/aws-iam-login/commit/0a16242c9be63d3a82cf721b30ae99fce2fa67a4))

* chore(deps): bump urllib3 from 1.26.16 to 1.26.17 (#108) ([`075a4d6`](https://github.com/conijnio/aws-iam-login/commit/075a4d6d68234e5f8d45ac8a7129bd128c7cf3d2))

* chore(deps): bump urllib3 from 1.26.16 to 1.26.17

Bumps [urllib3](https://github.com/urllib3/urllib3) from 1.26.16 to 1.26.17.
- [Release notes](https://github.com/urllib3/urllib3/releases)
- [Changelog](https://github.com/urllib3/urllib3/blob/main/CHANGES.rst)
- [Commits](https://github.com/urllib3/urllib3/compare/1.26.16...1.26.17)

---
updated-dependencies:
- dependency-name: urllib3
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`9cb5765`](https://github.com/conijnio/aws-iam-login/commit/9cb57655a433f6319ecc8497561bd858acb3ef95))

* chore(deps): bump boto3 from 1.28.57 to 1.28.58 (#107) ([`908a30d`](https://github.com/conijnio/aws-iam-login/commit/908a30d413e74fd31b4db6e6dcd3be48987b05a5))

* chore(deps): bump boto3 from 1.28.57 to 1.28.58

Bumps [boto3](https://github.com/boto/boto3) from 1.28.57 to 1.28.58.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.57...1.28.58)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`d8f479b`](https://github.com/conijnio/aws-iam-login/commit/d8f479bdbdf81372e5a9f525e7a93072c268806d))

* chore(deps): bump boto3 from 1.28.56 to 1.28.57 (#106) ([`5c762f6`](https://github.com/conijnio/aws-iam-login/commit/5c762f6ac2c9541e394c25b320d84b3f6f36fd46))

* chore(deps): bump boto3 from 1.28.56 to 1.28.57

Bumps [boto3](https://github.com/boto/boto3) from 1.28.56 to 1.28.57.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.56...1.28.57)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`97f23c6`](https://github.com/conijnio/aws-iam-login/commit/97f23c64fdf67b0ba6b527c2f7c75ac26515c2ac))

* chore(deps): bump boto3 from 1.28.55 to 1.28.56 (#105) ([`6345eb2`](https://github.com/conijnio/aws-iam-login/commit/6345eb23f302615e4ac7d6238a442b372547ee16))

* chore(deps): bump boto3 from 1.28.55 to 1.28.56

Bumps [boto3](https://github.com/boto/boto3) from 1.28.55 to 1.28.56.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.55...1.28.56)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`d10324f`](https://github.com/conijnio/aws-iam-login/commit/d10324fa2469bc3690ed8c27e0e1e585925a3891))

* chore(deps): bump boto3 from 1.28.54 to 1.28.55 (#104) ([`9c2deb2`](https://github.com/conijnio/aws-iam-login/commit/9c2deb2f53f334dc28b92dd993d1b4b263e65ca2))

* chore(deps): bump boto3 from 1.28.54 to 1.28.55

Bumps [boto3](https://github.com/boto/boto3) from 1.28.54 to 1.28.55.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.54...1.28.55)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`058f370`](https://github.com/conijnio/aws-iam-login/commit/058f370c52fb047160ba57c232346b5fe2da5384))

* chore(deps): bump boto3 from 1.28.53 to 1.28.54 (#103) ([`50fea8f`](https://github.com/conijnio/aws-iam-login/commit/50fea8f0c87f631ecd0bab974d819084fb06fa7c))

* chore(deps): bump boto3 from 1.28.53 to 1.28.54

Bumps [boto3](https://github.com/boto/boto3) from 1.28.53 to 1.28.54.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.53...1.28.54)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`ddca8dc`](https://github.com/conijnio/aws-iam-login/commit/ddca8dca6f78adc0f4e2f6195bd25f889fe154ca))

* chore(deps): bump boto3 from 1.28.52 to 1.28.53 (#102) ([`354a8ef`](https://github.com/conijnio/aws-iam-login/commit/354a8ef5c125fc72ab23b895740f6a89bd0667d3))

* chore(deps): bump boto3 from 1.28.52 to 1.28.53

Bumps [boto3](https://github.com/boto/boto3) from 1.28.52 to 1.28.53.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.52...1.28.53)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`69e0d9e`](https://github.com/conijnio/aws-iam-login/commit/69e0d9e97b7ecd6fcbab3efc0f2a6271fdb284a4))

* chore(deps-dev): bump cryptography from 41.0.3 to 41.0.4 (#101) ([`393c142`](https://github.com/conijnio/aws-iam-login/commit/393c1420448303691368823c0ce0fc58dc2be86f))

* chore(deps-dev): bump cryptography from 41.0.3 to 41.0.4

Bumps [cryptography](https://github.com/pyca/cryptography) from 41.0.3 to 41.0.4.
- [Changelog](https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pyca/cryptography/compare/41.0.3...41.0.4)

---
updated-dependencies:
- dependency-name: cryptography
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`226e3cd`](https://github.com/conijnio/aws-iam-login/commit/226e3cd3ca8132d91ea80bc1a2dbc64c9c1dbe51))

* chore(deps): bump boto3 from 1.28.51 to 1.28.52 (#100) ([`e8f7437`](https://github.com/conijnio/aws-iam-login/commit/e8f74374fcdaf3d426a367d49462ed428ad46e95))

* chore(deps): bump boto3 from 1.28.51 to 1.28.52

Bumps [boto3](https://github.com/boto/boto3) from 1.28.51 to 1.28.52.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.51...1.28.52)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`6859cd1`](https://github.com/conijnio/aws-iam-login/commit/6859cd1515422f36d13d2bccb5a117d088f0dcd4))

* chore(deps): bump boto3 from 1.28.50 to 1.28.51 (#99) ([`dd4daef`](https://github.com/conijnio/aws-iam-login/commit/dd4daefc18e59581c836f391c05114b3dc3af26f))

* chore(deps): bump boto3 from 1.28.50 to 1.28.51

Bumps [boto3](https://github.com/boto/boto3) from 1.28.50 to 1.28.51.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.50...1.28.51)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`5b47d60`](https://github.com/conijnio/aws-iam-login/commit/5b47d60c6da285065774d1ed879aeecb930b45ce))

* chore(deps): bump boto3 from 1.28.49 to 1.28.50 (#98) ([`13d51f6`](https://github.com/conijnio/aws-iam-login/commit/13d51f672da0bbc03e29d2da59a70bc441ebd00a))

* chore(deps): bump boto3 from 1.28.49 to 1.28.50

Bumps [boto3](https://github.com/boto/boto3) from 1.28.49 to 1.28.50.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.49...1.28.50)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`38180e0`](https://github.com/conijnio/aws-iam-login/commit/38180e07cda2659bcc04e3ab86ccf9e115e387e0))

* chore(deps): bump boto3 from 1.28.48 to 1.28.49 (#97) ([`ced0c4f`](https://github.com/conijnio/aws-iam-login/commit/ced0c4fa6b28974f075d8f62bee9dcc15116677a))

* chore(deps): bump boto3 from 1.28.48 to 1.28.49

Bumps [boto3](https://github.com/boto/boto3) from 1.28.48 to 1.28.49.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.48...1.28.49)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`26e958a`](https://github.com/conijnio/aws-iam-login/commit/26e958a627ccc7b85e987f321c58d7c603326b02))

* chore(deps): bump boto3 from 1.28.47 to 1.28.48 (#96) ([`1dbaad6`](https://github.com/conijnio/aws-iam-login/commit/1dbaad69c757aca6edab1032a05dd2a20049db49))

* chore(deps): bump boto3 from 1.28.47 to 1.28.48

Bumps [boto3](https://github.com/boto/boto3) from 1.28.47 to 1.28.48.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.47...1.28.48)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`65085ec`](https://github.com/conijnio/aws-iam-login/commit/65085ec2051a703539acc8073de4415417f46cb3))

* chore(deps): bump boto3 from 1.28.46 to 1.28.47 (#95) ([`6b69d77`](https://github.com/conijnio/aws-iam-login/commit/6b69d770221af05f340cca6031161120cbe38085))

* chore(deps): bump boto3 from 1.28.46 to 1.28.47

Bumps [boto3](https://github.com/boto/boto3) from 1.28.46 to 1.28.47.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.46...1.28.47)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`d96f12f`](https://github.com/conijnio/aws-iam-login/commit/d96f12fe636a2dd98bfe9dfbefa5dc3987690267))

* chore(deps): bump boto3 from 1.28.45 to 1.28.46 (#94) ([`033c9b8`](https://github.com/conijnio/aws-iam-login/commit/033c9b8d6b31a9a4f266b431af44b822d3d5ca6b))

* chore(deps): bump boto3 from 1.28.45 to 1.28.46

Bumps [boto3](https://github.com/boto/boto3) from 1.28.45 to 1.28.46.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.45...1.28.46)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`257967d`](https://github.com/conijnio/aws-iam-login/commit/257967d5ef598bf8ffe9b0e25794253c722e278c))

* chore(deps-dev): bump radon from 5.1.0 to 6.0.1 (#69) ([`cc487ba`](https://github.com/conijnio/aws-iam-login/commit/cc487ba1004b61575c7e9cc115635081dc6fab83))

* chore(deps-dev): bump radon from 5.1.0 to 6.0.1

Bumps [radon](https://github.com/rubik/radon) from 5.1.0 to 6.0.1.
- [Changelog](https://github.com/rubik/radon/blob/master/CHANGELOG)
- [Commits](https://github.com/rubik/radon/compare/v5.1.0...v6.0.1)

---
updated-dependencies:
- dependency-name: radon
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`68fac9c`](https://github.com/conijnio/aws-iam-login/commit/68fac9c7d93e545a6826195807bb810c9f8cda36))

* chore(deps-dev): bump black from 23.7.0 to 23.9.1 (#93) ([`c7aea7c`](https://github.com/conijnio/aws-iam-login/commit/c7aea7cba6c994428b5583729a5da03f702597af))

* chore(deps): bump boto3 from 1.28.44 to 1.28.45 (#92) ([`94db493`](https://github.com/conijnio/aws-iam-login/commit/94db49376706ae0884cf7cf59528e033734d6db5))

* chore(deps-dev): bump black from 23.7.0 to 23.9.1

Bumps [black](https://github.com/psf/black) from 23.7.0 to 23.9.1.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/23.7.0...23.9.1)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`f20f4f5`](https://github.com/conijnio/aws-iam-login/commit/f20f4f5087a4cc9d47e2e401543891122af703ba))

* chore(deps): bump boto3 from 1.28.44 to 1.28.45

Bumps [boto3](https://github.com/boto/boto3) from 1.28.44 to 1.28.45.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.44...1.28.45)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`df25162`](https://github.com/conijnio/aws-iam-login/commit/df251624ab4a7234819015842fdca7830e3e44b3))

* chore(deps): bump boto3 from 1.28.43 to 1.28.44 (#91) ([`f59a921`](https://github.com/conijnio/aws-iam-login/commit/f59a921b5240c7759bc927f95dd05a38647946f6))

* chore(deps): bump boto3 from 1.28.43 to 1.28.44

Bumps [boto3](https://github.com/boto/boto3) from 1.28.43 to 1.28.44.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.43...1.28.44)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`ae19656`](https://github.com/conijnio/aws-iam-login/commit/ae1965661d7e0d019baf4f29dba6e66f516fce09))

* chore(deps-dev): bump pytest from 7.4.1 to 7.4.2 (#89) ([`cd3fec5`](https://github.com/conijnio/aws-iam-login/commit/cd3fec5066655770f7da25dbfae0d2eeb2d6950a))

* chore(deps): bump boto3 from 1.28.42 to 1.28.43 (#90) ([`724593a`](https://github.com/conijnio/aws-iam-login/commit/724593a3978a6128a1fb6a4aaa3438a17d4af31b))

* chore(deps): bump boto3 from 1.28.42 to 1.28.43

Bumps [boto3](https://github.com/boto/boto3) from 1.28.42 to 1.28.43.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.42...1.28.43)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`26d3c52`](https://github.com/conijnio/aws-iam-login/commit/26d3c52fbc6349dd2d7c171320c4222e19950e61))

* chore(deps-dev): bump pytest from 7.4.1 to 7.4.2

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.4.1 to 7.4.2.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.4.1...7.4.2)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`0c78414`](https://github.com/conijnio/aws-iam-login/commit/0c78414532b9d786a880a6b20687a74a3c2bb1ef))

* chore(deps): bump boto3 from 1.28.41 to 1.28.42 (#88) ([`f1a885e`](https://github.com/conijnio/aws-iam-login/commit/f1a885ee8600a12c9cfc8b6e6431e85dc037b162))

* chore(deps): bump boto3 from 1.28.41 to 1.28.42

Bumps [boto3](https://github.com/boto/boto3) from 1.28.41 to 1.28.42.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.41...1.28.42)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`40e3cfa`](https://github.com/conijnio/aws-iam-login/commit/40e3cfa876db61e52b4596e54a760ead90fa09c4))

* chore(deps): bump boto3 from 1.28.40 to 1.28.41 (#87) ([`850bc4d`](https://github.com/conijnio/aws-iam-login/commit/850bc4d9fc31b053dc4518a3b31c4fa1b2edb5d1))

* chore(deps): bump boto3 from 1.28.40 to 1.28.41

Bumps [boto3](https://github.com/boto/boto3) from 1.28.40 to 1.28.41.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.40...1.28.41)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`690bc52`](https://github.com/conijnio/aws-iam-login/commit/690bc52e0fb1f9e1cba1c6d12e94fe950b9ebc20))

* chore(deps-dev): bump pytest from 7.4.0 to 7.4.1 (#86) ([`50f03bf`](https://github.com/conijnio/aws-iam-login/commit/50f03bfb342f80e206c1499484c66446fbf65f1c))

* chore(deps-dev): bump pytest from 7.4.0 to 7.4.1

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.4.0 to 7.4.1.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.4.0...7.4.1)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`51143f5`](https://github.com/conijnio/aws-iam-login/commit/51143f58847d6b078f674552274cc3968a4f1da1))

* chore(deps): bump boto3 from 1.28.39 to 1.28.40 (#85) ([`f31517f`](https://github.com/conijnio/aws-iam-login/commit/f31517fdd8ea53511556108ad540348221a8f93a))

* chore(deps): bump boto3 from 1.28.39 to 1.28.40

Bumps [boto3](https://github.com/boto/boto3) from 1.28.39 to 1.28.40.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.39...1.28.40)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`9040572`](https://github.com/conijnio/aws-iam-login/commit/9040572b22dbdfff2e750f5ce2564ba9bdee4a9d))

* chore(deps): bump boto3 from 1.28.38 to 1.28.39 (#84) ([`572086c`](https://github.com/conijnio/aws-iam-login/commit/572086c782ed65b38ab3b15a92da2ea40ac10640))

* chore(deps): bump boto3 from 1.28.38 to 1.28.39

Bumps [boto3](https://github.com/boto/boto3) from 1.28.38 to 1.28.39.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.38...1.28.39)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`f814d75`](https://github.com/conijnio/aws-iam-login/commit/f814d751859e4bd3b4c68d91f6b0c217c280c954))

* chore(deps): bump boto3 from 1.28.37 to 1.28.38 (#83) ([`d79f2af`](https://github.com/conijnio/aws-iam-login/commit/d79f2aff01a02c8e9dbba0e0edfcc64242aeb579))

* chore(deps): bump boto3 from 1.28.37 to 1.28.38

Bumps [boto3](https://github.com/boto/boto3) from 1.28.37 to 1.28.38.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.37...1.28.38)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`c077a28`](https://github.com/conijnio/aws-iam-login/commit/c077a28d359ea94b3d190725b38b24892f92aa3c))

* chore(deps): bump boto3 from 1.28.36 to 1.28.37 (#82) ([`a5a386d`](https://github.com/conijnio/aws-iam-login/commit/a5a386d52d582b4ae93fd52ae0fefb92a332962b))

* chore(deps): bump boto3 from 1.28.36 to 1.28.37

Bumps [boto3](https://github.com/boto/boto3) from 1.28.36 to 1.28.37.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.36...1.28.37)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`afdf463`](https://github.com/conijnio/aws-iam-login/commit/afdf46331535715eae09942c7cc0f5d7a410a28b))

* chore(deps): bump boto3 from 1.28.35 to 1.28.36 (#81) ([`928e3ab`](https://github.com/conijnio/aws-iam-login/commit/928e3abe84698608ec9a3571c3ba47f167e3b346))

* chore(deps): bump boto3 from 1.28.35 to 1.28.36

Bumps [boto3](https://github.com/boto/boto3) from 1.28.35 to 1.28.36.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.35...1.28.36)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`56ccaac`](https://github.com/conijnio/aws-iam-login/commit/56ccaacb93dc6a1b70625a3da12da1056ea423b6))

* chore(deps): bump boto3 from 1.28.34 to 1.28.35 (#80) ([`61e3092`](https://github.com/conijnio/aws-iam-login/commit/61e30929ef6135344cd7e619ea4b59d9fec934f3))

* chore(deps): bump boto3 from 1.28.34 to 1.28.35

Bumps [boto3](https://github.com/boto/boto3) from 1.28.34 to 1.28.35.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.34...1.28.35)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`edbcda1`](https://github.com/conijnio/aws-iam-login/commit/edbcda1426c8c63921550c25e71d762d3ddbadaf))

* chore(deps): bump boto3 from 1.28.33 to 1.28.34 (#79) ([`375ef8a`](https://github.com/conijnio/aws-iam-login/commit/375ef8a04f65400533b9402531932fc9c62a1845))

* chore(deps): bump boto3 from 1.28.33 to 1.28.34

Bumps [boto3](https://github.com/boto/boto3) from 1.28.33 to 1.28.34.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.33...1.28.34)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`9f3c29e`](https://github.com/conijnio/aws-iam-login/commit/9f3c29ea559311484dc8228e67dba6d7ab466c5e))

* chore(deps): bump boto3 from 1.28.32 to 1.28.33 (#78) ([`ef036b6`](https://github.com/conijnio/aws-iam-login/commit/ef036b66eece04e2d5dbcd702c44c1f1a1b5b19a))

* chore(deps): bump boto3 from 1.28.32 to 1.28.33

Bumps [boto3](https://github.com/boto/boto3) from 1.28.32 to 1.28.33.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.32...1.28.33)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`3bf766c`](https://github.com/conijnio/aws-iam-login/commit/3bf766c8ba1c9a36f4c135d0a279ff5f804fc35f))

* chore(deps): bump boto3 from 1.28.31 to 1.28.32 (#77) ([`2161948`](https://github.com/conijnio/aws-iam-login/commit/2161948f45abdcae46c04a077c7e5557add16494))

* chore(deps): bump boto3 from 1.28.31 to 1.28.32

Bumps [boto3](https://github.com/boto/boto3) from 1.28.31 to 1.28.32.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.31...1.28.32)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`10ff0c5`](https://github.com/conijnio/aws-iam-login/commit/10ff0c53d8c8f17aab22bc4894b25a0154cd54c0))

* chore(deps): bump boto3 from 1.28.30 to 1.28.31 (#76) ([`431675a`](https://github.com/conijnio/aws-iam-login/commit/431675a5412838fa25d276cd5bed6a602553b201))

* chore(deps): bump boto3 from 1.28.30 to 1.28.31

Bumps [boto3](https://github.com/boto/boto3) from 1.28.30 to 1.28.31.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.30...1.28.31)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`396c402`](https://github.com/conijnio/aws-iam-login/commit/396c402b607397eb712e09d3e40092178b304827))

* chore(deps): bump boto3 from 1.28.29 to 1.28.30 (#75) ([`73315b3`](https://github.com/conijnio/aws-iam-login/commit/73315b3e6b92a83260be635f677f843ede85a5f3))

* chore(deps): bump boto3 from 1.28.29 to 1.28.30

Bumps [boto3](https://github.com/boto/boto3) from 1.28.29 to 1.28.30.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.29...1.28.30)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`703d338`](https://github.com/conijnio/aws-iam-login/commit/703d338f0b9aa5082a9892d37fdd0c8f1858c150))

* chore(deps): bump boto3 from 1.28.28 to 1.28.29 (#74) ([`bef15fa`](https://github.com/conijnio/aws-iam-login/commit/bef15fabe9a9202b558d2ed45f395c661b428e2a))

* chore(deps): bump click from 8.1.6 to 8.1.7 (#73) ([`5bec609`](https://github.com/conijnio/aws-iam-login/commit/5bec6094df218ce830080820049f21ae533854ed))

* chore(deps): bump boto3 from 1.28.28 to 1.28.29

Bumps [boto3](https://github.com/boto/boto3) from 1.28.28 to 1.28.29.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.28...1.28.29)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`9207aa2`](https://github.com/conijnio/aws-iam-login/commit/9207aa23a6d35e26e7f47f5d7684bde8851d0588))

* chore(deps): bump click from 8.1.6 to 8.1.7

Bumps [click](https://github.com/pallets/click) from 8.1.6 to 8.1.7.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/main/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.1.6...8.1.7)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`cb7ab30`](https://github.com/conijnio/aws-iam-login/commit/cb7ab30e630b052174a97ad008028ca841c8d1e6))

* chore(deps-dev): bump mypy from 1.5.0 to 1.5.1 (#72) ([`bc05696`](https://github.com/conijnio/aws-iam-login/commit/bc0569656b0bdacd60e8389933df4ae96c170fc8))

* chore(deps): bump boto3 from 1.28.27 to 1.28.28 (#71) ([`7b1d613`](https://github.com/conijnio/aws-iam-login/commit/7b1d6138da96bf2b8e19c3eff006cc1faac298f9))

* chore(deps-dev): bump mypy from 1.5.0 to 1.5.1

Bumps [mypy](https://github.com/python/mypy) from 1.5.0 to 1.5.1.
- [Commits](https://github.com/python/mypy/compare/v1.5.0...v1.5.1)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`f17890b`](https://github.com/conijnio/aws-iam-login/commit/f17890bb430b8556ed0d9ef7cfcd1ca24f7b62da))

* chore(deps): bump boto3 from 1.28.27 to 1.28.28

Bumps [boto3](https://github.com/boto/boto3) from 1.28.27 to 1.28.28.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.27...1.28.28)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`bc28ed8`](https://github.com/conijnio/aws-iam-login/commit/bc28ed82406de096ea6f45af283c1caa48611786))

* chore(deps): bump boto3 from 1.28.26 to 1.28.27 (#70) ([`6ab110b`](https://github.com/conijnio/aws-iam-login/commit/6ab110bd924cc954cecacbf2ae1673d10de87e34))

* chore(deps): bump boto3 from 1.28.26 to 1.28.27

Bumps [boto3](https://github.com/boto/boto3) from 1.28.26 to 1.28.27.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.26...1.28.27)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`e7b75f9`](https://github.com/conijnio/aws-iam-login/commit/e7b75f9979ed01c93ba7f35f499a0f14d79f300b))

* chore(deps): bump boto3 from 1.28.25 to 1.28.26 (#68) ([`2588ce1`](https://github.com/conijnio/aws-iam-login/commit/2588ce1ab32b7cc7919e680f1a8ba54fb8248b33))

* chore(deps-dev): bump xenon from 0.9.0 to 0.9.1 (#67) ([`a345426`](https://github.com/conijnio/aws-iam-login/commit/a345426748f53a069266b9c69bc37b9f3b55a86a))

* chore(deps): bump boto3 from 1.28.25 to 1.28.26

Bumps [boto3](https://github.com/boto/boto3) from 1.28.25 to 1.28.26.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.25...1.28.26)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`8895c8c`](https://github.com/conijnio/aws-iam-login/commit/8895c8c13cef350eae2ed462be9f895f8ab21eef))

* chore(deps-dev): bump xenon from 0.9.0 to 0.9.1

Bumps [xenon](https://github.com/rubik/xenon) from 0.9.0 to 0.9.1.
- [Changelog](https://github.com/rubik/xenon/blob/master/CHANGELOG)
- [Commits](https://github.com/rubik/xenon/compare/v0.9.0...v0.9.1)

---
updated-dependencies:
- dependency-name: xenon
  dependency-type: direct:development
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`db2671e`](https://github.com/conijnio/aws-iam-login/commit/db2671e13e1e886752c44d7e5ebff036b94403a4))

* chore(deps): bump boto3 from 1.28.24 to 1.28.25 (#66) ([`c274387`](https://github.com/conijnio/aws-iam-login/commit/c274387ce3d9b96aa0638ff9dcba74fc5d6e263d))

* chore(deps): bump boto3 from 1.28.24 to 1.28.25

Bumps [boto3](https://github.com/boto/boto3) from 1.28.24 to 1.28.25.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.24...1.28.25)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`aa0f9a9`](https://github.com/conijnio/aws-iam-login/commit/aa0f9a92ce5a6f9b4ad0bd9795f93f5a96d325bd))

* chore: update dependencies ([`f3ecd26`](https://github.com/conijnio/aws-iam-login/commit/f3ecd26dee90e242d2e2f13f5ca4065ecbecd2e5))

* chore(deps): bump boto3 from 1.28.23 to 1.28.24 (#64) ([`8909b1e`](https://github.com/conijnio/aws-iam-login/commit/8909b1ea2bc3888a827a8e489bdd2add2d4756db))

* chore(deps): bump boto3 from 1.28.23 to 1.28.24

Bumps [boto3](https://github.com/boto/boto3) from 1.28.23 to 1.28.24.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.23...1.28.24)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`9d2635d`](https://github.com/conijnio/aws-iam-login/commit/9d2635db42098433e64fc6f55bce9698b4c6b2aa))

* chore(deps): bump boto3 from 1.28.22 to 1.28.23 (#63) ([`6c44718`](https://github.com/conijnio/aws-iam-login/commit/6c4471836df9826b30e437ea00b5b581d4f0e551))

* chore(deps): bump boto3 from 1.28.22 to 1.28.23

Bumps [boto3](https://github.com/boto/boto3) from 1.28.22 to 1.28.23.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.22...1.28.23)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`321d0fa`](https://github.com/conijnio/aws-iam-login/commit/321d0fa0e1dabfa4ec3441368bb000fda31dcd73))

* chore(deps): bump boto3 from 1.28.21 to 1.28.22 (#62) ([`9e14dec`](https://github.com/conijnio/aws-iam-login/commit/9e14decd12cc17567d8ec4f4f1846d4ebb5d227f))

* chore(deps): bump boto3 from 1.28.21 to 1.28.22

Bumps [boto3](https://github.com/boto/boto3) from 1.28.21 to 1.28.22.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.21...1.28.22)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`bc9a7c6`](https://github.com/conijnio/aws-iam-login/commit/bc9a7c6b939a24ee8b2914d6bca720776d8f2e4c))

* chore(deps): bump boto3 from 1.28.20 to 1.28.21 (#61) ([`a2dbb45`](https://github.com/conijnio/aws-iam-login/commit/a2dbb45cc17fe7b77e8999a89864b0424df3eb6c))

* chore(deps): bump boto3 from 1.28.20 to 1.28.21

Bumps [boto3](https://github.com/boto/boto3) from 1.28.20 to 1.28.21.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.20...1.28.21)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`0d5dcc2`](https://github.com/conijnio/aws-iam-login/commit/0d5dcc2a57e62c6699a1d1a9a447c6f0a47d1858))

* chore(deps): bump boto3 from 1.28.19 to 1.28.20 (#60) ([`eb35915`](https://github.com/conijnio/aws-iam-login/commit/eb359152f3ba350f06b41b91b44bfbab747c9d3b))

* chore(deps): bump boto3 from 1.28.19 to 1.28.20

Bumps [boto3](https://github.com/boto/boto3) from 1.28.19 to 1.28.20.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.19...1.28.20)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`f1bed3c`](https://github.com/conijnio/aws-iam-login/commit/f1bed3caea93ee3e57a41e0bf93b0c4f53153002))

### Fix

* fix: ci/cd process after move to conijnio ([`6ea0e8c`](https://github.com/conijnio/aws-iam-login/commit/6ea0e8c188dfbad7a99b81b3e2ac7c5fefd167e9))

### Unknown

* Update dependabot.yml ([`ccf9956`](https://github.com/conijnio/aws-iam-login/commit/ccf99565fd4b1a43285e0c8e720c6f9a0e6c0fbf))


## v0.3.3 (2023-08-04)

### Chore

* chore(deps): bump boto3 from 1.28.18 to 1.28.19 (#58) ([`b3106b6`](https://github.com/conijnio/aws-iam-login/commit/b3106b675f76645d31f93a90de8f6ba2465191cc))

* chore(deps): bump boto3 from 1.28.18 to 1.28.19

Bumps [boto3](https://github.com/boto/boto3) from 1.28.18 to 1.28.19.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.18...1.28.19)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`2684651`](https://github.com/conijnio/aws-iam-login/commit/268465143b3ba128eb85c5c03b0cabb96dd233e0))

* chore(deps): bump boto3 from 1.28.17 to 1.28.18 (#57) ([`1e29810`](https://github.com/conijnio/aws-iam-login/commit/1e29810b6c7c85e517ed1fe77c32ca136b4ca073))

* chore(deps): bump boto3 from 1.28.17 to 1.28.18

Bumps [boto3](https://github.com/boto/boto3) from 1.28.17 to 1.28.18.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.17...1.28.18)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`28ae1b1`](https://github.com/conijnio/aws-iam-login/commit/28ae1b1a84b9c14fd04bc5c3e66836645930a6bf))

* chore(deps): bump boto3 from 1.28.16 to 1.28.17 (#56) ([`5277e6d`](https://github.com/conijnio/aws-iam-login/commit/5277e6d6d45d176018a8fcb99696724af86b00a1))

* chore(deps): bump boto3 from 1.28.16 to 1.28.17

Bumps [boto3](https://github.com/boto/boto3) from 1.28.16 to 1.28.17.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.16...1.28.17)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`c9d3cd4`](https://github.com/conijnio/aws-iam-login/commit/c9d3cd449176dd6b81c412df76b954dc1ac4150c))

* chore(deps): bump boto3 from 1.28.15 to 1.28.16 (#55) ([`f88a15d`](https://github.com/conijnio/aws-iam-login/commit/f88a15d07151b4f8a2d06b204754b8f711d8dafd))

* chore(deps): bump boto3 from 1.28.15 to 1.28.16

Bumps [boto3](https://github.com/boto/boto3) from 1.28.15 to 1.28.16.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.15...1.28.16)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`a8ae42e`](https://github.com/conijnio/aws-iam-login/commit/a8ae42e9876846fa5f6bd0dc84f22f39f89521ad))

* chore(deps): bump boto3 from 1.28.14 to 1.28.15 (#54) ([`d209bb9`](https://github.com/conijnio/aws-iam-login/commit/d209bb9e2da3f81227c168a1479232929621d8d4))

* chore(deps): bump boto3 from 1.28.14 to 1.28.15

Bumps [boto3](https://github.com/boto/boto3) from 1.28.14 to 1.28.15.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.14...1.28.15)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`953f8ca`](https://github.com/conijnio/aws-iam-login/commit/953f8cadbb80970d5d036c6a3f26d33029096f22))

* chore(deps): bump the dependencies group with 1 update (#52) ([`c5bd41f`](https://github.com/conijnio/aws-iam-login/commit/c5bd41f7283ab53c1f5202626f7888f0efa96377))

* chore(deps): bump the dependencies group with 1 update

Bumps the dependencies group with 1 update: [boto3](https://github.com/boto/boto3).

- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.13...1.28.14)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
  dependency-group: dependencies
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`290f18d`](https://github.com/conijnio/aws-iam-login/commit/290f18dba2355ca2b5028746eb698eec0878f62b))

* chore: group dependencies and assign code owner ([`1cec4b5`](https://github.com/conijnio/aws-iam-login/commit/1cec4b5ad4e18ca4fde7f73b250e0568d4bd26e5))

* chore: fix auto-merge ([`fa3cb06`](https://github.com/conijnio/aws-iam-login/commit/fa3cb06fa16195f0468baf04efe059198e0b4199))

* chore(deps): bump boto3 from 1.28.12 to 1.28.13 (#51) ([`241c0d8`](https://github.com/conijnio/aws-iam-login/commit/241c0d84c15182bd6dcfa25615d72c12601579dc))

* chore(deps): bump boto3 from 1.28.12 to 1.28.13

Bumps [boto3](https://github.com/boto/boto3) from 1.28.12 to 1.28.13.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.12...1.28.13)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`98aa282`](https://github.com/conijnio/aws-iam-login/commit/98aa2820a85834c463b412cfceae8e6dce9fce63))

* chore(deps): bump boto3 from 1.28.10 to 1.28.12 (#50) ([`d0eb3a3`](https://github.com/conijnio/aws-iam-login/commit/d0eb3a39cdadf71b4ffafe805407224206a247da))

* chore(deps): bump boto3 from 1.28.10 to 1.28.12

Bumps [boto3](https://github.com/boto/boto3) from 1.28.10 to 1.28.12.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.10...1.28.12)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`1227e50`](https://github.com/conijnio/aws-iam-login/commit/1227e50f078669728a01345abfae427cf0e14a25))

* chore(deps): bump boto3 from 1.28.9 to 1.28.10 (#48) ([`ccc9899`](https://github.com/conijnio/aws-iam-login/commit/ccc9899518337efa645dbd540e973e9413ab2b5a))

* chore(deps): bump boto3 from 1.28.9 to 1.28.10

Bumps [boto3](https://github.com/boto/boto3) from 1.28.9 to 1.28.10.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.9...1.28.10)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`73b4604`](https://github.com/conijnio/aws-iam-login/commit/73b46043f1b4327ecbd6af46247f5d8884ebdaa5))

* chore(deps): bump boto3 from 1.28.8 to 1.28.9 (#47) ([`be7dbdf`](https://github.com/conijnio/aws-iam-login/commit/be7dbdfaed70b930425194e4128f4d8d04ea1075))

* chore(deps): bump boto3 from 1.28.8 to 1.28.9

Bumps [boto3](https://github.com/boto/boto3) from 1.28.8 to 1.28.9.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.8...1.28.9)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`7067f13`](https://github.com/conijnio/aws-iam-login/commit/7067f132d06e9d183e62bcda93de3d699ecfea7c))

* chore(deps): bump boto3 from 1.28.6 to 1.28.8 (#46) ([`85c17ef`](https://github.com/conijnio/aws-iam-login/commit/85c17ef3092f11998bed58eaa66fe935e65d0d4c))

* chore(deps): bump boto3 from 1.28.6 to 1.28.8

Bumps [boto3](https://github.com/boto/boto3) from 1.28.6 to 1.28.8.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.6...1.28.8)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`d89629b`](https://github.com/conijnio/aws-iam-login/commit/d89629b5cc83954236733e4c1701eabe585ccd6d))

* chore: change license to apache 2.0 ([`50cd222`](https://github.com/conijnio/aws-iam-login/commit/50cd222fece5f2165253cd77343a577126606d91))

* chore: enable auto-commit for dependabot pull requests (#45)

**Issue #, if available:**

## Description of changes:

&lt;!--- One or two sentences as a summary of what&#39;s being changed --&gt;

**Checklist**

&lt;!--- Leave unchecked if your change doesn&#39;t seem to apply --&gt;

* [ ] Update tests
* [ ] Update docs
* [x] PR title follows [conventional commit
semantics](https://www.conventionalcommits.org/en/v1.0.0-beta.2/#commit-message-for-a-fix-using-an-optional-issue-number)

By submitting this pull request, I confirm that you can use, modify,
copy, and redistribute this contribution, under the terms of your
choice. ([`0fd01a6`](https://github.com/conijnio/aws-iam-login/commit/0fd01a64d59952a1ce4fdf91f6ba8a84653a453c))

* chore: enable auto-commit for dependabot pull requests ([`f030f40`](https://github.com/conijnio/aws-iam-login/commit/f030f406481ab15f2fae9ad4341c288d431b671b))

* chore(deps): bump boto3 from 1.28.5 to 1.28.6 (#44) ([`b5694b7`](https://github.com/conijnio/aws-iam-login/commit/b5694b71632d0e588e87e66d1e82a32f909a15d3))

* chore(deps): bump boto3 from 1.28.5 to 1.28.6

Bumps [boto3](https://github.com/boto/boto3) from 1.28.5 to 1.28.6.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.5...1.28.6)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`130aeb1`](https://github.com/conijnio/aws-iam-login/commit/130aeb166946a4bb3379e4cbe0e19556417b289d))

* chore(deps): bump boto3 from 1.28.3 to 1.28.5 (#43) ([`d50e31d`](https://github.com/conijnio/aws-iam-login/commit/d50e31dfdaa4e74b1ed1d92f7f776a3925b22d7b))

* chore(deps): bump click from 8.1.5 to 8.1.6 (#42) ([`0e4ab1c`](https://github.com/conijnio/aws-iam-login/commit/0e4ab1caf7983908416a32f3a3e85c5d17d9e1de))

* chore(deps): bump boto3 from 1.28.3 to 1.28.5

Bumps [boto3](https://github.com/boto/boto3) from 1.28.3 to 1.28.5.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.3...1.28.5)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`d175ced`](https://github.com/conijnio/aws-iam-login/commit/d175ced1def1fde9f9145ef53e2d05001f2670d1))

* chore(deps): bump click from 8.1.5 to 8.1.6

Bumps [click](https://github.com/pallets/click) from 8.1.5 to 8.1.6.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/8.1.6/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.1.5...8.1.6)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`7fcf5e8`](https://github.com/conijnio/aws-iam-login/commit/7fcf5e882381ec4ba2364582cb77fc72ddf6c551))

* chore(deps): bump boto3 from 1.28.2 to 1.28.3 (#41) ([`4aa0890`](https://github.com/conijnio/aws-iam-login/commit/4aa0890a3cf1167c7c2ac54bf68993faa8ef9390))

* chore(deps): bump click from 8.1.4 to 8.1.5 (#40) ([`918df1d`](https://github.com/conijnio/aws-iam-login/commit/918df1d653a03f0f37d8e451374bc2f1da7677e7))

* chore(deps): bump boto3 from 1.28.2 to 1.28.3

Bumps [boto3](https://github.com/boto/boto3) from 1.28.2 to 1.28.3.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.2...1.28.3)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`ed64e90`](https://github.com/conijnio/aws-iam-login/commit/ed64e90e14c2478a913763979755b26603a2ea37))

* chore(deps): bump click from 8.1.4 to 8.1.5

Bumps [click](https://github.com/pallets/click) from 8.1.4 to 8.1.5.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/8.1.5/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.1.4...8.1.5)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`e179d0f`](https://github.com/conijnio/aws-iam-login/commit/e179d0fee5379d986de5b6dbede457e5ee0e54a6))

* chore(deps): bump boto3 from 1.28.1 to 1.28.2 (#39) ([`e3a5aee`](https://github.com/conijnio/aws-iam-login/commit/e3a5aee3bd3a32097088417e3ea3b95806877c38))

* chore(deps-dev): bump black from 23.3.0 to 23.7.0 (#38) ([`457db76`](https://github.com/conijnio/aws-iam-login/commit/457db763277238f2ec2770bdba3bde39a8e118c3))

* chore(deps): bump boto3 from 1.28.1 to 1.28.2

Bumps [boto3](https://github.com/boto/boto3) from 1.28.1 to 1.28.2.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.1...1.28.2)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`748506e`](https://github.com/conijnio/aws-iam-login/commit/748506e3b57543ba6149cc41c9ad46c433db653b))

* chore(deps-dev): bump black from 23.3.0 to 23.7.0

Bumps [black](https://github.com/psf/black) from 23.3.0 to 23.7.0.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/23.3.0...23.7.0)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`95a65e7`](https://github.com/conijnio/aws-iam-login/commit/95a65e77e34169e1c4c25ede882d0e3419c4df77))

### Fix

* fix: update dependencies (#59)

**Issue #, if available:**

## Description of changes:

Manually update all dependencies

**Checklist**

&lt;!--- Leave unchecked if your change doesn&#39;t seem to apply --&gt;

* [ ] Update tests
* [ ] Update docs
* [x] PR title follows [conventional commit
semantics](https://www.conventionalcommits.org/en/v1.0.0-beta.2/#commit-message-for-a-fix-using-an-optional-issue-number)

By submitting this pull request, I confirm that you can use, modify,
copy, and redistribute this contribution, under the terms of your
choice. ([`1e74040`](https://github.com/conijnio/aws-iam-login/commit/1e7404085ee5b90e884a07d258fa475860c04bd7))

* fix: update dependencies

Manually update all dependencies ([`c228b87`](https://github.com/conijnio/aws-iam-login/commit/c228b8785005ed9a9e7ad9392bccd4aa8a967673))

### Unknown

* Update dependabot.yml ([`4870b57`](https://github.com/conijnio/aws-iam-login/commit/4870b57f518ed84f0d2aeadf29186c3c42c1256f))

* Update auto-merge.yml ([`8998653`](https://github.com/conijnio/aws-iam-login/commit/8998653efb2244cb8955227f7d5d6fa8c366d51a))

* Update auto-merge.yml ([`b20766b`](https://github.com/conijnio/aws-iam-login/commit/b20766b3f14789dcf73fdd9cf8c7ab875b696b78))


## v0.3.2 (2023-07-11)

### Chore

* chore(deps): bump click from 8.1.3 to 8.1.4 (#36)

Bumps [click](https://github.com/pallets/click) from 8.1.3 to 8.1.4.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pallets/click/releases&#34;&gt;click&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;8.1.4&lt;/h2&gt;
&lt;p&gt;This is a fix release for the 8.1.x feature branch.&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Changes: &lt;a
href=&#34;https://click.palletsprojects.com/en/8.1.x/changes/#version-8-1-4&#34;&gt;https://click.palletsprojects.com/en/8.1.x/changes/#version-8-1-4&lt;/a&gt;&lt;/li&gt;
&lt;li&gt;Milestone: &lt;a
href=&#34;https://github.com/pallets/click/milestone/19?closed=1&#34;&gt;https://github.com/pallets/click/milestone/19?closed=1&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/pallets/click/blob/main/CHANGES.rst&#34;&gt;click&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;Version 8.1.4&lt;/h2&gt;
&lt;p&gt;Released 2023-07-06&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;Replace all &lt;code&gt;typing.Dict&lt;/code&gt; occurrences to
&lt;code&gt;typing.MutableMapping&lt;/code&gt; for
parameter hints. :issue:&lt;code&gt;2255&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Improve type hinting for decorators and give all generic types
parameters.
:issue:&lt;code&gt;2398&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Fix return value and type signature of
&lt;code&gt;shell_completion.add_completion_class&lt;/code&gt;
function. :pr:&lt;code&gt;2421&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Bash version detection doesn&#39;t fail on Windows.
:issue:&lt;code&gt;2461&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Completion works if there is a dot (&lt;code&gt;.&lt;/code&gt;) in the program
name. :issue:&lt;code&gt;2166&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Improve type annotations for pyright type checker.
:issue:&lt;code&gt;2268&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Improve responsiveness of &lt;code&gt;click.clear()&lt;/code&gt;.
:issue:&lt;code&gt;2284&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Improve command name detection when using Shiv or PEX.
:issue:&lt;code&gt;2332&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Avoid showing empty lines if command help text is empty.
:issue:&lt;code&gt;2368&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;ZSH completion script works when loaded from &lt;code&gt;fpath&lt;/code&gt;.
:issue:&lt;code&gt;2344&lt;/code&gt;.&lt;/li&gt;
&lt;li&gt;&lt;code&gt;EOFError&lt;/code&gt; and &lt;code&gt;KeyboardInterrupt&lt;/code&gt; tracebacks
are not suppressed when
&lt;code&gt;standalone_mode&lt;/code&gt; is disabled. :issue:&lt;code&gt;2380&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;&lt;code&gt;@group.command&lt;/code&gt; does not fail if the group was created
with a custom
&lt;code&gt;command_class&lt;/code&gt;. :issue:&lt;code&gt;2416&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;&lt;code&gt;multiple=True&lt;/code&gt; is allowed for flag options again and
does not require
setting &lt;code&gt;default=()&lt;/code&gt;. :issue:&lt;code&gt;2246, 2292,
2295&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Make the decorators returned by &lt;code&gt;@argument()&lt;/code&gt; and
&lt;code&gt;@option()&lt;/code&gt; reusable when the
&lt;code&gt;cls&lt;/code&gt; parameter is used. :issue:&lt;code&gt;2294&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Don&#39;t fail when writing filenames to streams with strict errors.
Replace invalid
bytes with the replacement character (&lt;code&gt;�&lt;/code&gt;).
:issue:&lt;code&gt;2395&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Remove unnecessary attempt to detect MSYS2 environment.
:issue:&lt;code&gt;2355&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Remove outdated and unnecessary detection of App Engine environment.
:pr:&lt;code&gt;2554&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;&lt;code&gt;echo()&lt;/code&gt; does not fail when no streams are attached, such
as with &lt;code&gt;pythonw&lt;/code&gt; on
Windows. :issue:&lt;code&gt;2415&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;Argument with &lt;code&gt;expose_value=False&lt;/code&gt; do not cause
completion to fail. :issue:&lt;code&gt;2336&lt;/code&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/blockquote&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/3d873a3f567d1bbcb6fb25f0fbe3c3128488d99d&#34;&gt;&lt;code&gt;3d873a3&lt;/code&gt;&lt;/a&gt;
release version 8.1.4&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/dd691da8028a090657f081b584ce1efb1bb149d2&#34;&gt;&lt;code&gt;dd691da&lt;/code&gt;&lt;/a&gt;
use pypi trusted publisher auth&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/b67fe5f70a8c88bf54d6c7058b1154a81d32815c&#34;&gt;&lt;code&gt;b67fe5f&lt;/code&gt;&lt;/a&gt;
completion doesn&#39;t fail with &lt;code&gt;expose_value=False&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/pallets/click/issues/2556&#34;&gt;#2556&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/4cf7c6cdb10e441da775b4a3a7ee55caec83249e&#34;&gt;&lt;code&gt;4cf7c6c&lt;/code&gt;&lt;/a&gt;
completion works for expose_value=False&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/549947111c4af2191dd4b245e1de2c25d20c36d6&#34;&gt;&lt;code&gt;5499471&lt;/code&gt;&lt;/a&gt;
echo doesn&#39;t fail with no streams (&lt;a
href=&#34;https://redirect.github.com/pallets/click/issues/2555&#34;&gt;#2555&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/ecb99836a44367bad62960045d586e31e4a95766&#34;&gt;&lt;code&gt;ecb9983&lt;/code&gt;&lt;/a&gt;
echo doesn&#39;t fail with no streams&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/9a536eebd958558c2cd24c17fb66fac112f1ac91&#34;&gt;&lt;code&gt;9a536ee&lt;/code&gt;&lt;/a&gt;
remove msys2 and app engine detection (&lt;a
href=&#34;https://redirect.github.com/pallets/click/issues/2554&#34;&gt;#2554&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/daca3cfce4dcc98451362da0785e4db5fd2b1d8a&#34;&gt;&lt;code&gt;daca3cf&lt;/code&gt;&lt;/a&gt;
remove app engine detection&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/8f019ba54eb6838c182c8bfe9310a8d526602071&#34;&gt;&lt;code&gt;8f019ba&lt;/code&gt;&lt;/a&gt;
remove msys2 detection&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/pallets/click/commit/af1e8d44d64181484a60dd63044da706bcc13439&#34;&gt;&lt;code&gt;af1e8d4&lt;/code&gt;&lt;/a&gt;
&lt;code&gt;format_filename&lt;/code&gt; replaces invalid bytes (&lt;a
href=&#34;https://redirect.github.com/pallets/click/issues/2553&#34;&gt;#2553&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/pallets/click/compare/8.1.3...8.1.4&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=click&amp;package-manager=pip&amp;previous-version=8.1.3&amp;new-version=8.1.4)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt; ([`bfbea48`](https://github.com/conijnio/aws-iam-login/commit/bfbea48b167fb3fbbb310efcd646b21b4772baef))

* chore(deps): bump boto3 from 1.28.0 to 1.28.1 (#37) ([`1d9c708`](https://github.com/conijnio/aws-iam-login/commit/1d9c70838213550e0860ced567ebf0296a1f96dc))

* chore(deps): bump boto3 from 1.28.0 to 1.28.1

Bumps [boto3](https://github.com/boto/boto3) from 1.28.0 to 1.28.1.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.28.0...1.28.1)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`7673cab`](https://github.com/conijnio/aws-iam-login/commit/7673cab67f465ac576bd0f1b9e05c64173f434fb))

* chore(deps): bump click from 8.1.3 to 8.1.4

Bumps [click](https://github.com/pallets/click) from 8.1.3 to 8.1.4.
- [Release notes](https://github.com/pallets/click/releases)
- [Changelog](https://github.com/pallets/click/blob/main/CHANGES.rst)
- [Commits](https://github.com/pallets/click/compare/8.1.3...8.1.4)

---
updated-dependencies:
- dependency-name: click
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`5ffe2e3`](https://github.com/conijnio/aws-iam-login/commit/5ffe2e39ad744557aac331f10c0e5f3a0d7a6d99))

* chore(deps): bump boto3 from 1.27.1 to 1.28.0 (#35) ([`27275c7`](https://github.com/conijnio/aws-iam-login/commit/27275c7e9a5a4752bde77ecb74f206b9541db9ce))

* chore(deps): bump boto3 from 1.27.1 to 1.28.0

Bumps [boto3](https://github.com/boto/boto3) from 1.27.1 to 1.28.0.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.27.1...1.28.0)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`344b0a3`](https://github.com/conijnio/aws-iam-login/commit/344b0a3d5c0b2b64634cb67bb69853059f88dc47))

* chore(deps): bump boto3 from 1.27.0 to 1.27.1 (#34) ([`8ad4679`](https://github.com/conijnio/aws-iam-login/commit/8ad467909e956f3992c8f8743de96f512b9ea5a2))

* chore(deps): bump boto3 from 1.27.0 to 1.27.1

Bumps [boto3](https://github.com/boto/boto3) from 1.27.0 to 1.27.1.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.27.0...1.27.1)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`44740e2`](https://github.com/conijnio/aws-iam-login/commit/44740e26bac248f4c18736bc6aebb50b5516d927))

* chore(deps): bump boto3 from 1.26.165 to 1.27.0 (#33) ([`19a2ce9`](https://github.com/conijnio/aws-iam-login/commit/19a2ce98e827c20caba65a348bdf2b2b82e3c0c7))

* chore(deps): bump boto3 from 1.26.165 to 1.27.0

Bumps [boto3](https://github.com/boto/boto3) from 1.26.165 to 1.27.0.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.26.165...1.27.0)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`f0308dc`](https://github.com/conijnio/aws-iam-login/commit/f0308dcbcef2451489b2f523b81d9d98d064ef3f))

* chore(deps): bump boto3 from 1.26.164 to 1.26.165 (#32) ([`e44d1ef`](https://github.com/conijnio/aws-iam-login/commit/e44d1ef5508557195416700e50cdba9b5cdb83e8))

* chore(deps): bump boto3 from 1.26.164 to 1.26.165

Bumps [boto3](https://github.com/boto/boto3) from 1.26.164 to 1.26.165.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.26.164...1.26.165)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`8da963f`](https://github.com/conijnio/aws-iam-login/commit/8da963ff428c535bb950b38bda4dd2a25849850a))

* chore(deps): bump boto3 from 1.26.163 to 1.26.164 (#31) ([`1c84d18`](https://github.com/conijnio/aws-iam-login/commit/1c84d18d783481bc55f0dd34318b18afd37dea48))

* chore(deps): bump boto3 from 1.26.163 to 1.26.164

Bumps [boto3](https://github.com/boto/boto3) from 1.26.163 to 1.26.164.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.26.163...1.26.164)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`4140dde`](https://github.com/conijnio/aws-iam-login/commit/4140dde42f92fc5c484e08eb955566d7cc070c22))

* chore(deps): bump boto3 from 1.26.162 to 1.26.163 (#30) ([`7fa248d`](https://github.com/conijnio/aws-iam-login/commit/7fa248d33ab88c42cf4d6b6432463fa3fbf86032))

* chore(deps): bump boto3 from 1.26.162 to 1.26.163

Bumps [boto3](https://github.com/boto/boto3) from 1.26.162 to 1.26.163.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.26.162...1.26.163)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`58700ad`](https://github.com/conijnio/aws-iam-login/commit/58700ad9acf4c56e91a6092bf7f333223b08fa3d))

* chore(deps): bump boto3 from 1.26.161 to 1.26.162 (#29) ([`57cbef8`](https://github.com/conijnio/aws-iam-login/commit/57cbef8568710632c8e49cd261c534e85cc7655f))

* chore(deps): bump boto3 from 1.26.161 to 1.26.162

Bumps [boto3](https://github.com/boto/boto3) from 1.26.161 to 1.26.162.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.26.161...1.26.162)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`252ceee`](https://github.com/conijnio/aws-iam-login/commit/252ceee1eca9177e18552015e389da15aa49f921))

* chore(deps): bump boto3 from 1.26.84 to 1.26.161 (#27)

Bumps [boto3](https://github.com/boto/boto3) from 1.26.84 to 1.26.161.
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/boto/boto3/blob/develop/CHANGELOG.rst&#34;&gt;boto3&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h1&gt;1.26.161&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;connect&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release provides a way to search for existing tags within an instance.
Before tagging a resource, ensure consistency by searching for
pre-existing key:value pairs.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;glue&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Timestamp
Starting Position For Kinesis and Kafka Data Sources in a Glue Streaming
Job&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;guardduty&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Add
support for user.extra.sessionName in Kubernetes Audit Logs
Findings.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;iam&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Support for a
new API &amp;quot;GetMFADevice&amp;quot; to present MFA device metadata such as
device certifications&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;pinpoint&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added time
zone estimation support for journeys&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.26.160&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;devops-guru&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds support for encryption via customer managed keys.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;fsx&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update to
Amazon FSx documentation.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;rds&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Documentation
improvements for create, describe, and modify DB clusters and DB
instances.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;verifiedpermissions&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Added improved descriptions and new code samples to SDK
documentation.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.26.159&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;chime-sdk-identity&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
AppInstanceBots can be configured to be invoked or not using the Target
or the CHIME.mentions attribute for ChannelMessages&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;chime-sdk-messaging&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
ChannelMessages can be made visible to sender and intended recipient
rather than all channel members with the target attribute. For example,
a user can send messages to a bot and receive messages back in a group
channel without other members seeing them.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;kendra&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Introducing
Amazon Kendra Retrieve API that can be used to retrieve relevant
passages or text excerpts given an input query.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;stepfunctions&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Update stepfunctions client to latest version&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.26.158&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;dynamodb&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;]
Documentation updates for DynamoDB&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;emr&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Update emr
client to latest version&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;inspector2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds support for Software Bill of Materials (SBOM) export and
the general availability of code scanning for AWS Lambda functions.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;mediaconvert&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release introduces the bandwidth reduction filter for the HEVC encoder,
increases the limits of outputs per job, and updates support for the
Nagra SDK to version 1.14.7.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;mq&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] The Cross Region
Disaster Recovery feature allows to replicate a brokers state from one
region to another in order to provide customers with multi-region
resiliency in the event of a regional outage.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;sagemaker&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release provides support in SageMaker for output files in training jobs
to be uploaded without compression and enable customer to deploy
uncompressed model from S3 to real-time inference Endpoints. In
addition, ml.trn1n.32xlarge is added to supported instance type list in
training job.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;transfer&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds a new parameter StructuredLogDestinations to CreateServer,
UpdateServer APIs.&lt;/li&gt;
&lt;/ul&gt;
&lt;h1&gt;1.26.157&lt;/h1&gt;
&lt;ul&gt;
&lt;li&gt;api-change:&lt;code&gt;appflow&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This
release adds new API to reset connector metadata cache&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;config&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Updated
ResourceType enum with new resource types onboarded by AWS Config in May
2023.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;ec2&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Adds support
for targeting Dedicated Host allocations by assetIds in AWS
Outposts&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;lambda&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] This release
adds RecursiveInvocationException to the Invoke API and
InvokeWithResponseStream API.&lt;/li&gt;
&lt;li&gt;api-change:&lt;code&gt;redshift&lt;/code&gt;: [&lt;code&gt;botocore&lt;/code&gt;] Added
support for custom domain names for Redshift Provisioned clusters. This
feature enables customers to create a custom domain name and use ACM to
generate fully secure connections to it.&lt;/li&gt;
&lt;/ul&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/4b03b73ba84fd3c088215357849defd8409bb255&#34;&gt;&lt;code&gt;4b03b73&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.26.161&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/2a25ff388495d2821229b8c95555a8469b343dbf&#34;&gt;&lt;code&gt;2a25ff3&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.26.161&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/06e70009eef78a02c7237e80a43001371d997c25&#34;&gt;&lt;code&gt;06e7000&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/ac432a61ab668da0bf1df940f64a25bf1d0f37a5&#34;&gt;&lt;code&gt;ac432a6&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.26.160&#39; into develop&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/c0d4f4ac23917df5aec0b79d9f36cc1e778d60f5&#34;&gt;&lt;code&gt;c0d4f4a&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.26.160&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/252234ebb7d43f639e05425ce439baeb6b3afabd&#34;&gt;&lt;code&gt;252234e&lt;/code&gt;&lt;/a&gt;
Bumping version to 1.26.160&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/21d63f007668040c05cd91d6bdeb27f88f8900a9&#34;&gt;&lt;code&gt;21d63f0&lt;/code&gt;&lt;/a&gt;
Add changelog entries from botocore&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/762e8fb611d34f7e399e00be3b9bb70f078c289f&#34;&gt;&lt;code&gt;762e8fb&lt;/code&gt;&lt;/a&gt;
chore: update ancient issue bot (&lt;a
href=&#34;https://redirect.github.com/boto/boto3/issues/3734&#34;&gt;#3734&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/0c110bd66ebc00384222936ce7db6c6b058bfcec&#34;&gt;&lt;code&gt;0c110bd&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.26.159&#39;&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/boto/boto3/commit/169f44b3978e27a3bd8de09616007b450d00baa0&#34;&gt;&lt;code&gt;169f44b&lt;/code&gt;&lt;/a&gt;
Merge branch &#39;release-1.26.159&#39; into develop&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/boto/boto3/compare/1.26.84...1.26.161&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=boto3&amp;package-manager=pip&amp;previous-version=1.26.84&amp;new-version=1.26.161)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt; ([`8f3fd5d`](https://github.com/conijnio/aws-iam-login/commit/8f3fd5de5bc137d7af8ae4375289da83fc1b4372))

* chore(deps): bump boto3 from 1.26.84 to 1.26.161

Bumps [boto3](https://github.com/boto/boto3) from 1.26.84 to 1.26.161.
- [Release notes](https://github.com/boto/boto3/releases)
- [Changelog](https://github.com/boto/boto3/blob/develop/CHANGELOG.rst)
- [Commits](https://github.com/boto/boto3/compare/1.26.84...1.26.161)

---
updated-dependencies:
- dependency-name: boto3
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`3302999`](https://github.com/conijnio/aws-iam-login/commit/3302999aae8c946655790808acd65510ee628f0c))

* chore(deps-dev): bump pytest-cov from 3.0.0 to 4.1.0 (#28) ([`9719e68`](https://github.com/conijnio/aws-iam-login/commit/9719e68cb4a43f34dac8b15db17d7571d07890a2))

* chore(deps-dev): bump pytest-cov from 3.0.0 to 4.1.0

Bumps [pytest-cov](https://github.com/pytest-dev/pytest-cov) from 3.0.0 to 4.1.0.
- [Changelog](https://github.com/pytest-dev/pytest-cov/blob/master/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest-cov/compare/v3.0.0...v4.1.0)

---
updated-dependencies:
- dependency-name: pytest-cov
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`6459860`](https://github.com/conijnio/aws-iam-login/commit/6459860a763ab380a6e56e264364172387a3a790))

* chore(deps-dev): bump black from 22.12.0 to 23.3.0 (#26)

Bumps [black](https://github.com/psf/black) from 22.12.0 to 23.3.0.
&lt;details&gt;
&lt;summary&gt;Release notes&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/releases&#34;&gt;black&#39;s
releases&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.3.0&lt;/h2&gt;
&lt;h3&gt;Highlights&lt;/h3&gt;
&lt;p&gt;This release fixes a longstanding confusing behavior in Black&#39;s
GitHub action, where the
version of the action did not determine the version of Black being run
(issue &lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3382&#34;&gt;#3382&lt;/a&gt;). In
addition, there is a small bug fix around imports and a number of
improvements to the
preview style.&lt;/p&gt;
&lt;p&gt;Please try out the
&lt;a
href=&#34;https://black.readthedocs.io/en/stable/the_black_code_style/future_style.html#preview-style&#34;&gt;preview
style&lt;/a&gt;
with &lt;code&gt;black --preview&lt;/code&gt; and tell us your feedback. All changes
in the preview style are
expected to become part of Black&#39;s stable style in January 2024.&lt;/p&gt;
&lt;h3&gt;Stable style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Import lines with &lt;code&gt;# fmt: skip&lt;/code&gt; and &lt;code&gt;# fmt:
off&lt;/code&gt; no longer have an extra blank line
added when they are right after another import line (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3610&#34;&gt;#3610&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Add trailing commas to collection literals even if there&#39;s a comment
after the last
entry (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3393&#34;&gt;#3393&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;code&gt;async def&lt;/code&gt;, &lt;code&gt;async for&lt;/code&gt;, and &lt;code&gt;async
with&lt;/code&gt; statements are now formatted consistently
compared to their non-async version. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3609&#34;&gt;#3609&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;code&gt;with&lt;/code&gt; statements that contain two context managers will
be consistently wrapped in
parentheses (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3589&#34;&gt;#3589&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Let string splitters respect &lt;a
href=&#34;https://www.unicode.org/reports/tr11/&#34;&gt;East Asian Width&lt;/a&gt;
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3445&#34;&gt;#3445&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Now long string literals can be split after East Asian commas and
periods (&lt;code&gt;、&lt;/code&gt; U+3001
IDEOGRAPHIC COMMA, &lt;code&gt;。&lt;/code&gt; U+3002 IDEOGRAPHIC FULL STOP, &amp;amp;
&lt;code&gt;，&lt;/code&gt; U+FF0C FULLWIDTH COMMA)
besides before spaces (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3445&#34;&gt;#3445&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;For stubs, enforce one blank line after a nested class with a body
other than just
&lt;code&gt;...&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3564&#34;&gt;#3564&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Improve handling of multiline strings by changing line split
behavior (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/1879&#34;&gt;#1879&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Parser&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Added support for formatting files with invalid type comments (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3594&#34;&gt;#3594&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Update GitHub Action to use the version of Black equivalent to
action&#39;s version if
version input is not specified (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3543&#34;&gt;#3543&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix missing Python binary path in autoload script for vim (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3508&#34;&gt;#3508&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Documentation&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Document that only the most recent release is supported for security
issues;
vulnerabilities should be reported through Tidelift (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3612&#34;&gt;#3612&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Changelog&lt;/summary&gt;
&lt;p&gt;&lt;em&gt;Sourced from &lt;a
href=&#34;https://github.com/psf/black/blob/main/CHANGES.md&#34;&gt;black&#39;s
changelog&lt;/a&gt;.&lt;/em&gt;&lt;/p&gt;
&lt;blockquote&gt;
&lt;h2&gt;23.3.0&lt;/h2&gt;
&lt;h3&gt;Highlights&lt;/h3&gt;
&lt;p&gt;This release fixes a longstanding confusing behavior in Black&#39;s
GitHub action, where the
version of the action did not determine the version of Black being run
(issue &lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3382&#34;&gt;#3382&lt;/a&gt;). In
addition, there is a small bug fix around imports and a number of
improvements to the
preview style.&lt;/p&gt;
&lt;p&gt;Please try out the
&lt;a
href=&#34;https://black.readthedocs.io/en/stable/the_black_code_style/future_style.html#preview-style&#34;&gt;preview
style&lt;/a&gt;
with &lt;code&gt;black --preview&lt;/code&gt; and tell us your feedback. All changes
in the preview style are
expected to become part of Black&#39;s stable style in January 2024.&lt;/p&gt;
&lt;h3&gt;Stable style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Import lines with &lt;code&gt;# fmt: skip&lt;/code&gt; and &lt;code&gt;# fmt:
off&lt;/code&gt; no longer have an extra blank line
added when they are right after another import line (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3610&#34;&gt;#3610&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Preview style&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Add trailing commas to collection literals even if there&#39;s a comment
after the last
entry (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3393&#34;&gt;#3393&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;code&gt;async def&lt;/code&gt;, &lt;code&gt;async for&lt;/code&gt;, and &lt;code&gt;async
with&lt;/code&gt; statements are now formatted consistently
compared to their non-async version. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3609&#34;&gt;#3609&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;code&gt;with&lt;/code&gt; statements that contain two context managers will
be consistently wrapped in
parentheses (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3589&#34;&gt;#3589&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Let string splitters respect &lt;a
href=&#34;https://www.unicode.org/reports/tr11/&#34;&gt;East Asian Width&lt;/a&gt;
(&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3445&#34;&gt;#3445&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Now long string literals can be split after East Asian commas and
periods (&lt;code&gt;、&lt;/code&gt; U+3001
IDEOGRAPHIC COMMA, &lt;code&gt;。&lt;/code&gt; U+3002 IDEOGRAPHIC FULL STOP, &amp;amp;
&lt;code&gt;，&lt;/code&gt; U+FF0C FULLWIDTH COMMA)
besides before spaces (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3445&#34;&gt;#3445&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;For stubs, enforce one blank line after a nested class with a body
other than just
&lt;code&gt;...&lt;/code&gt; (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3564&#34;&gt;#3564&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Improve handling of multiline strings by changing line split
behavior (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/1879&#34;&gt;#1879&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Parser&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Added support for formatting files with invalid type comments (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3594&#34;&gt;#3594&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Integrations&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Update GitHub Action to use the version of Black equivalent to
action&#39;s version if
version input is not specified (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3543&#34;&gt;#3543&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Fix missing Python binary path in autoload script for vim (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3508&#34;&gt;#3508&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;h3&gt;Documentation&lt;/h3&gt;
&lt;ul&gt;
&lt;li&gt;Document that only the most recent release is supported for security
issues;
vulnerabilities should be reported through Tidelift (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3612&#34;&gt;#3612&lt;/a&gt;)&lt;/li&gt;
&lt;/ul&gt;
&lt;!-- raw HTML omitted --&gt;
&lt;/blockquote&gt;
&lt;p&gt;... (truncated)&lt;/p&gt;
&lt;/details&gt;
&lt;details&gt;
&lt;summary&gt;Commits&lt;/summary&gt;
&lt;ul&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/bf7a16254ec96b084a6caf3d435ec18f0f245cc7&#34;&gt;&lt;code&gt;bf7a162&lt;/code&gt;&lt;/a&gt;
Fixup the changelog (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3628&#34;&gt;#3628&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/9b2b048692f0bd642f38230b4e61c778a4653f91&#34;&gt;&lt;code&gt;9b2b048&lt;/code&gt;&lt;/a&gt;
Prepare release 23.3.0 (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3625&#34;&gt;#3625&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/bf5abdb0b6cf6644628977230736a0a6478c1bff&#34;&gt;&lt;code&gt;bf5abdb&lt;/code&gt;&lt;/a&gt;
Specify Python exec path with minor version if available (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3508&#34;&gt;#3508&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/b542f589a5c4041f54847591104cd51684849f2e&#34;&gt;&lt;code&gt;b542f58&lt;/code&gt;&lt;/a&gt;
Use GH action version when version argument not specified (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3543&#34;&gt;#3543&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/f3b1a3b9d2fc6de8f0845399cb80d8bdfd6400fd&#34;&gt;&lt;code&gt;f3b1a3b&lt;/code&gt;&lt;/a&gt;
Bump furo from 2022.12.7 to 2023.3.23 in /docs (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3624&#34;&gt;#3624&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/ef6e079901d53a42dfae4ab10b081ce7a73a47b5&#34;&gt;&lt;code&gt;ef6e079&lt;/code&gt;&lt;/a&gt;
Let string splitters respect &lt;code&gt;East_Asian_Width&lt;/code&gt; property (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3445&#34;&gt;#3445&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/5c064a986c388e2be1e448c3e4b28e5f5ba7ce5a&#34;&gt;&lt;code&gt;5c064a9&lt;/code&gt;&lt;/a&gt;
Bump sphinx from 5.3.0 to 6.1.3 in /docs (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3499&#34;&gt;#3499&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/3a9d6f0a5f9013b97676f3d24246bd34d93fce4c&#34;&gt;&lt;code&gt;3a9d6f0&lt;/code&gt;&lt;/a&gt;
Bump myst-parser from 0.18.1 to 1.0.0 in /docs (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3601&#34;&gt;#3601&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/53c23e62df9b182edf9e7ccf726acdcf8c25846f&#34;&gt;&lt;code&gt;53c23e6&lt;/code&gt;&lt;/a&gt;
Support files with type comment syntax errors (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3594&#34;&gt;#3594&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;&lt;a
href=&#34;https://github.com/psf/black/commit/dba3c2695c59fdb11825dbdf8f3b0ab6e0b368b2&#34;&gt;&lt;code&gt;dba3c26&lt;/code&gt;&lt;/a&gt;
Fix bug introduced in &lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3564&#34;&gt;#3564&lt;/a&gt;. (&lt;a
href=&#34;https://redirect.github.com/psf/black/issues/3615&#34;&gt;#3615&lt;/a&gt;)&lt;/li&gt;
&lt;li&gt;Additional commits viewable in &lt;a
href=&#34;https://github.com/psf/black/compare/22.12.0...23.3.0&#34;&gt;compare
view&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;
&lt;/details&gt;
&lt;br /&gt;


[![Dependabot compatibility
score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=black&amp;package-manager=pip&amp;previous-version=22.12.0&amp;new-version=23.3.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores)

Dependabot will resolve any conflicts with this PR as long as you don&#39;t
alter it yourself. You can also trigger a rebase manually by commenting
`@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

&lt;details&gt;
&lt;summary&gt;Dependabot commands and options&lt;/summary&gt;
&lt;br /&gt;

You can trigger Dependabot actions by commenting on this PR:
- `@dependabot rebase` will rebase this PR
- `@dependabot recreate` will recreate this PR, overwriting any edits
that have been made to it
- `@dependabot merge` will merge this PR after your CI passes on it
- `@dependabot squash and merge` will squash and merge this PR after
your CI passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
and block automerging
- `@dependabot reopen` will reopen this PR if it is closed
- `@dependabot close` will close this PR and stop Dependabot recreating
it. You can achieve the same result by closing it manually
- `@dependabot ignore this major version` will close this PR and stop
Dependabot creating any more for this major version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this PR and stop
Dependabot creating any more for this minor version (unless you reopen
the PR or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this PR and stop
Dependabot creating any more for this dependency (unless you reopen the
PR or upgrade to it yourself)


&lt;/details&gt; ([`aea12b9`](https://github.com/conijnio/aws-iam-login/commit/aea12b93d743a6344419326cbe44d3216581fce4))

* chore(deps-dev): bump black from 22.12.0 to 23.3.0

Bumps [black](https://github.com/psf/black) from 22.12.0 to 23.3.0.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/22.12.0...23.3.0)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`179686b`](https://github.com/conijnio/aws-iam-login/commit/179686bfb89ecd933e9f414f1b7f9891c3359a21))

* chore(deps-dev): bump pytest from 7.2.2 to 7.4.0

Bumps [pytest](https://github.com/pytest-dev/pytest) from 7.2.2 to 7.4.0.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/7.2.2...7.4.0)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:development
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`b18f079`](https://github.com/conijnio/aws-iam-login/commit/b18f0790ca2ca71f86f69dd1d86fa99448ba7dd8))

* chore(deps-dev): bump mypy from 0.961 to 1.4.1

Bumps [mypy](https://github.com/python/mypy) from 0.961 to 1.4.1.
- [Commits](https://github.com/python/mypy/compare/v0.961...v1.4.1)

---
updated-dependencies:
- dependency-name: mypy
  dependency-type: direct:development
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`46b6b17`](https://github.com/conijnio/aws-iam-login/commit/46b6b17471659dacdce278b1c62cb0f013625e80))

* chore(deps): bump cryptography from 39.0.2 to 41.0.0

Bumps [cryptography](https://github.com/pyca/cryptography) from 39.0.2 to 41.0.0.
- [Changelog](https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pyca/cryptography/compare/39.0.2...41.0.0)

---
updated-dependencies:
- dependency-name: cryptography
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`da36c68`](https://github.com/conijnio/aws-iam-login/commit/da36c681a329f2e50d16cf697e8d6816df6c2e4f))

* chore(deps): bump requests from 2.28.2 to 2.31.0

Bumps [requests](https://github.com/psf/requests) from 2.28.2 to 2.31.0.
- [Release notes](https://github.com/psf/requests/releases)
- [Changelog](https://github.com/psf/requests/blob/main/HISTORY.md)
- [Commits](https://github.com/psf/requests/compare/v2.28.2...v2.31.0)

---
updated-dependencies:
- dependency-name: requests
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`54774d9`](https://github.com/conijnio/aws-iam-login/commit/54774d946a01247de8e40ab598da6a403935a723))

### Fix

* fix: ignore the click decorators for mypy and remove main() call ([`d315151`](https://github.com/conijnio/aws-iam-login/commit/d3151516fe4b67aa630447dcc67a3b0b090fd0b5))

### Unknown

* Merge pull request #25 from Nr18/dependabot/pip/pytest-7.4.0

chore(deps-dev): bump pytest from 7.2.2 to 7.4.0 ([`c7bf7a9`](https://github.com/conijnio/aws-iam-login/commit/c7bf7a9240c4b3af34457133afa28b58c93bf655))

* Merge pull request #24 from Nr18/dependabot/pip/mypy-1.4.1

chore(deps-dev): bump mypy from 0.961 to 1.4.1 ([`31ef0e5`](https://github.com/conijnio/aws-iam-login/commit/31ef0e58a3a4592a790b708af5067cd433261b35))

* 0.3.1 ([`7882e30`](https://github.com/conijnio/aws-iam-login/commit/7882e30967aff4ce13cc7518ff5890ef8ee5d297))

* Merge branch &#39;develop&#39; ([`53af195`](https://github.com/conijnio/aws-iam-login/commit/53af195d1d689084a8aed93181d8f1e541992705))

* Update dependabot.yml ([`122d9d6`](https://github.com/conijnio/aws-iam-login/commit/122d9d6748ae575e3ab46354d9ea48e31755f0ef))

* Merge pull request #23 from Nr18/dependabot/pip/cryptography-41.0.0 ([`69070f5`](https://github.com/conijnio/aws-iam-login/commit/69070f5e0643e843bfb0766454f5d2b80793cbf4))

* Merge pull request #22 from Nr18/dependabot/pip/requests-2.31.0 ([`7eaa251`](https://github.com/conijnio/aws-iam-login/commit/7eaa251419ddf0271c51512a9e28647ae2d5912e))


## v0.3.1 (2023-03-06)

### Chore

* chore: version bump ([`ce7ec1c`](https://github.com/conijnio/aws-iam-login/commit/ce7ec1c37be49a3d43efdcb212f771a1b9dbdc21))

### Fix

* fix: use proper project name ([`7fd573c`](https://github.com/conijnio/aws-iam-login/commit/7fd573c4e1a36e7c51fd29d755c149b0d64dfda8))

### Unknown

* Merge pull request #21 from Nr18/develop

chore: version bump ([`984dd66`](https://github.com/conijnio/aws-iam-login/commit/984dd667e433495f5fd20fc985e4648e2f2704a4))

* Merge pull request #20 from Nr18/develop

fix: use proper project name ([`0f23e88`](https://github.com/conijnio/aws-iam-login/commit/0f23e88738cf1a10d34b7afcbfddf77f439f51ab))


## v0.3.0 (2023-03-06)

### Chore

* chore: version bump ([`4c8eb8d`](https://github.com/conijnio/aws-iam-login/commit/4c8eb8daf90fd95f26739bf0e26cc10b63723591))

* chore: version bump (#15) ([`c51616f`](https://github.com/conijnio/aws-iam-login/commit/c51616f4d307fca6dc17f675466bbd70bb337548))

* chore(deps): bump cryptography from 39.0.0 to 39.0.1 (#14) ([`f18365d`](https://github.com/conijnio/aws-iam-login/commit/f18365d4b81dbb48a23c0b6519e3fbf495daadd3))

* chore(deps): bump future from 0.18.2 to 0.18.3 (#13)

* chore(deps): bump future from 0.18.2 to 0.18.3

Bumps [future](https://github.com/PythonCharmers/python-future) from 0.18.2 to 0.18.3.
- [Release notes](https://github.com/PythonCharmers/python-future/releases)
- [Changelog](https://github.com/PythonCharmers/python-future/blob/master/docs/changelog.rst)
- [Commits](https://github.com/PythonCharmers/python-future/compare/v0.18.2...v0.18.3)

---
updated-dependencies:
- dependency-name: future
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;

* chore: update poetry and update poetry lock

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: Joris Conijn &lt;joris@conijnonline.nl&gt; ([`f8b77a5`](https://github.com/conijnio/aws-iam-login/commit/f8b77a576bc90f81ad88ba40a03fffd5bf09526e))

* chore(deps): bump cryptography from 37.0.4 to 38.0.3

Bumps [cryptography](https://github.com/pyca/cryptography) from 37.0.4 to 38.0.3.
- [Release notes](https://github.com/pyca/cryptography/releases)
- [Changelog](https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pyca/cryptography/compare/37.0.4...38.0.3)

---
updated-dependencies:
- dependency-name: cryptography
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`e6bcb52`](https://github.com/conijnio/aws-iam-login/commit/e6bcb5243608ab7d497a8161c99fdf52848c1256))

* chore(deps): bump certifi from 2022.6.15 to 2022.12.7

Bumps [certifi](https://github.com/certifi/python-certifi) from 2022.6.15 to 2022.12.7.
- [Release notes](https://github.com/certifi/python-certifi/releases)
- [Commits](https://github.com/certifi/python-certifi/compare/2022.06.15...2022.12.07)

---
updated-dependencies:
- dependency-name: certifi
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`2755488`](https://github.com/conijnio/aws-iam-login/commit/2755488066da2b358d345ccd1ec396e9bd0d7e4e))

### Feature

* feat: add help target ([`85838f0`](https://github.com/conijnio/aws-iam-login/commit/85838f06d0beb43f5064b68c88f1696e85de9ccb))

### Fix

* fix: use a explicit poetry version ([`4ae1baa`](https://github.com/conijnio/aws-iam-login/commit/4ae1baa5819ce65de221728df2e206dc05e0bac4))

* fix: typo ([`299bda7`](https://github.com/conijnio/aws-iam-login/commit/299bda7163920575e8034642d04d8bb2640c95ad))

### Unknown

* Merge pull request #19 from Nr18/develop

chore: version bump ([`d311171`](https://github.com/conijnio/aws-iam-login/commit/d311171158f42274f4b8eb690b06ce90d48f8887))

* Merge pull request #18 from Nr18/develop

fix: use a explicit poetry version ([`e0bcdec`](https://github.com/conijnio/aws-iam-login/commit/e0bcdec803f5866e3f4d06957a331e12278fca6a))

* Merge branch &#39;main&#39; into develop ([`092f403`](https://github.com/conijnio/aws-iam-login/commit/092f403777448b3e7876352813c1973a76d3f9a3))

* Merge pull request #17 from Nr18/fix/poetry

fix: use a explicit poetry version ([`a7924d3`](https://github.com/conijnio/aws-iam-login/commit/a7924d395b213f38cafd3609aafc7d8a3c8f8508))

* release: 0.3.0 (#16)

* chore(deps): bump certifi from 2022.6.15 to 2022.12.7

Bumps [certifi](https://github.com/certifi/python-certifi) from 2022.6.15 to 2022.12.7.
- [Release notes](https://github.com/certifi/python-certifi/releases)
- [Commits](https://github.com/certifi/python-certifi/compare/2022.06.15...2022.12.07)

---
updated-dependencies:
- dependency-name: certifi
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;

* chore(deps): bump cryptography from 37.0.4 to 38.0.3

Bumps [cryptography](https://github.com/pyca/cryptography) from 37.0.4 to 38.0.3.
- [Release notes](https://github.com/pyca/cryptography/releases)
- [Changelog](https://github.com/pyca/cryptography/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pyca/cryptography/compare/37.0.4...38.0.3)

---
updated-dependencies:
- dependency-name: cryptography
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;

* fix: typo

* feat: add help target

* chore(deps): bump future from 0.18.2 to 0.18.3 (#13)

* chore(deps): bump future from 0.18.2 to 0.18.3

Bumps [future](https://github.com/PythonCharmers/python-future) from 0.18.2 to 0.18.3.
- [Release notes](https://github.com/PythonCharmers/python-future/releases)
- [Changelog](https://github.com/PythonCharmers/python-future/blob/master/docs/changelog.rst)
- [Commits](https://github.com/PythonCharmers/python-future/compare/v0.18.2...v0.18.3)

---
updated-dependencies:
- dependency-name: future
  dependency-type: indirect
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;

* chore: update poetry and update poetry lock

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt;
Co-authored-by: Joris Conijn &lt;joris@conijnonline.nl&gt;

* chore(deps): bump cryptography from 39.0.0 to 39.0.1 (#14)

* chore: version bump (#15)

---------

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`6513804`](https://github.com/conijnio/aws-iam-login/commit/6513804af30dec8fe6d814c144ab432fcf14bc3f))

* Merge pull request #12 from Nr18/dependabot/pip/cryptography-38.0.3

chore(deps): bump cryptography from 37.0.4 to 38.0.3 ([`132017f`](https://github.com/conijnio/aws-iam-login/commit/132017f0d2b808d53ba691ac2f9b36f5f1891f85))

* Merge pull request #11 from Nr18/dependabot/pip/certifi-2022.12.7 ([`b4dd738`](https://github.com/conijnio/aws-iam-login/commit/b4dd738d4254524e0858e83b6f08cd126e39f1b1))


## v0.2.0 (2022-07-22)

### Chore

* chore: version bump (#7) ([`545a89f`](https://github.com/conijnio/aws-iam-login/commit/545a89fa7213363d6cc46668c7188c093048fde7))

### Feature

* feat: support initialization of configuration

By using the `get_caller_identity` API call. We can automatically configure the `username` and `mfa_serial` for the given access keys. This makes the tool it easier to use! ([`f70b033`](https://github.com/conijnio/aws-iam-login/commit/f70b03309f6dfe381a8b8351abb8fa6592d0ff90))

* feat: support access key rotation

By supporting access key rotation we will make it easier to rotate keys. This change will remove the barrier for rotating keys by making it easy to do.
When you make it easy to do people are more willing to perform an action. ([`bdb3fc2`](https://github.com/conijnio/aws-iam-login/commit/bdb3fc250a9ae63ffe68119880f3d441358327fd))

### Fix

* fix: resolve package name (#9)

By including the coverage configuration in the `pyproject.toml` file. The name of the project did not resolve correctly. By adding the ` =` we ensure that it is actually the correct name. ([`fdc8e66`](https://github.com/conijnio/aws-iam-login/commit/fdc8e66b99e335b9c4e0647f1df186f139ec43b4))

* fix: sample command to rotate credentials (#5) ([`74ef154`](https://github.com/conijnio/aws-iam-login/commit/74ef154acd62fb4164ed546b2fbc19aebcd4cd05))

### Refactor

* refactor: credential and access key cleanup (#6)

* refactor: split credentials in credentials and temp credentials
* refactor: use credentials in access key
* refactor: data sanitisation for access key and credentials ([`6f65330`](https://github.com/conijnio/aws-iam-login/commit/6f65330dae9d6e0b8bed1000d864cb6eec7f6a43))

### Unknown

* Merge pull request #10 from Nr18/develop

fix: resolve package name (#9) ([`b89040b`](https://github.com/conijnio/aws-iam-login/commit/b89040bbde2b4fa9c446382605dbf458f6ffefc6))

* Merge pull request #8 from Nr18/develop

release: 0.2.0 ([`d1ffac5`](https://github.com/conijnio/aws-iam-login/commit/d1ffac5cc0f37bf517a02cb85b0c360b3d19e68f))

* Merge pull request #4 from Nr18/feat/initialize

feat: support initialization of configuration ([`1d63e24`](https://github.com/conijnio/aws-iam-login/commit/1d63e24e9a00a4dcab7d30742c5fd95411bcacda))

* Merge pull request #3 from Nr18/feat/rotate-access-key

feat: support access key rotation ([`4690f63`](https://github.com/conijnio/aws-iam-login/commit/4690f6345aec37b9a18b1d44388f9feaa4992b86))

* Merge branch &#39;develop&#39; into feat/rotate-access-key ([`cec031f`](https://github.com/conijnio/aws-iam-login/commit/cec031fd4fdf06c23c0bd35a5a383d599bf34ed3))


## v0.1.1 (2022-07-06)

### Chore

* chore: release 0.1.1 ([`f1d9f3f`](https://github.com/conijnio/aws-iam-login/commit/f1d9f3ffeffe7ccf6a6ee447651f320c65724f88))

### Feature

* feat: initial commit ([`8d125c4`](https://github.com/conijnio/aws-iam-login/commit/8d125c4f041bf9fe6079d8e6d792a771f55cbb6d))

### Unknown

* Merge pull request #2 from Nr18/develop

chore: release 0.1.1 ([`2d964dd`](https://github.com/conijnio/aws-iam-login/commit/2d964dd6cc853aa2d092104f36aab9d10d5402b4))

* Merge pull request #1 from Nr18/chore/release-version

chore: release 0.1.1 ([`c7a8e6a`](https://github.com/conijnio/aws-iam-login/commit/c7a8e6a4be506993bf473c6b235aa0112876dcc4))
