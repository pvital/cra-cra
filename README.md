# cra-cra
Another Python web crawler.

This is a POC for print the sitemap of a given URL and depth 0.

## How to execute

```
$ python cracra.py https://fedoramagazine.org/taking-smart-backups-duplicity/
Getting info for https://fedoramagazine.org/taking-smart-backups-duplicity/
	 |-> https://fedoramagazine.org
	 |-> https://aws.amazon.com/iam
	 |-> http://fedoramagazine.org/submit-an-idea-or-tip
	 |-> https://fedoramagazine.org/taking-smart-backups-duplicity/
	 |-> https://fedoramagazine.org/submit-an-idea-or-tip/
	 |-> http://duplicity.nongnu.org/duplicity.1.html
	 |-> https://fedoraproject.org/wiki/Communicating_and_getting_help
	 |-> https://cdn.fedoramagazine.org/wp-content/uploads/2017/07/aws_full-1.png
	 |-> https://fedoramagazine.org/enhancing-smart-backups-duply/
	 |-> https://fedoramagazine.org/terms-and-conditions/
	 |-> https://fedoramagazine.org/taking-smart-backups-duplicity/#comment-473580
	 |-> https://fedoramagazine.org/tag/backups/
	 |-> https://fedoramagazine.org/creating-a-featured-image-for-a-fedora-magazine-article/
	 |-> http://duplicity.nongnu.org/
	 |-> https://fedoramagazine.org/taking-smart-backups-duplicity/#comment-473566
	 |-> http://fedoramagazine.org/writing-an-article-for-the-fedora-magazine/
	 |-> https://admin.fedoraproject.org/mailman/listinfo/marketing
	 |-> https://fedoramagazine.org/category/software/
	 |-> https://fedoramagazine.org/how-to-structure-your-article/
	 |-> https://fedoramagazine.org/tag/duplicity/
	 |-> https://fedoramagazine.org/taking-smart-backups-duplicity/#comment-473522
	 |-> https://fedoramagazine.org/writing-a-new-pitch/
	 |-> https://fedoramagazine.org/easy-backups-with-deja-dup/
	 |-> http://sourceforge.net/projects/librsync
	 |-> https://fedoramagazine.org/taking-smart-backups-duplicity/#comment-473430
	 |-> https://borgbackup.readthedocs.io/en/stable/
	 |-> http://www.gnupg.org/
	 |-> https://fedoramagazine.org/writing-an-article-for-the-fedora-magazine/
	 |-> https://fedoramagazine.org/taking-smart-backups-duplicity/#comment-473594
	 |-> https://fedoramagazine.org/publishing-workflow/
	 |-> https://getfedora.org/code-of-conduct
	 |-> http://cmp.felk.cvut.cz/~smidm/
	 |-> https://restic.github.io/
	 |-> https://fedoramagazine.org/gpg-key-management-part-1/
	 |-> https://fedoramagazine.org/tag/cloud/
	 |-> https://fedoramagazine.org/tips-for-articles/
	 |-> https://fedoramagazine.org/tag/amazon-web-services-aws/
	 |-> https://fedoramagazine.org/contact-us/
	 |-> https://cdn.fedoramagazine.org/wp-content/uploads/2017/07/aws_inc.png
	 |-> https://fedoramagazine.org/taking-smart-backups-duplicity/#comment-473738
	 |-> https://fedoramagazine.org/category/for-system-administrators/
	 |_

$
```

## TODO

See [enhancement's issues](https://github.com/pvital/cra-cra/issues?utf8=✓&q=is%3Aissue is%3Aopen label%3Aenhancement) to know the next steps of development.

Make cra-cra bigger and open any issue with the label *enhancement* to request something new.
