---
title: Launching
summary: How I published this Jekyll-based site from my local Windows 7 PC to a Linux-based server using Git.
description: How I published this Jekyll-based site from my local Windows 7 PC to a Linux-based server using Git.
date: 2013-04-21
---

## Getting Started

### Installing Ruby on Windows

Let's cover the easy bits first. Installing Ruby 1.9.3 on Windows 7 is, as of
this writing, tremendously simple. All one needs to do is navigate to the
[Windows Ruby Installer](http://rubyinstaller.org/), download the executable and
run it. The rest is pretty straightforward. If you don't get it, go away.

I like a decent terminal window. Sadly, Windows doesn't offer such a thing. You
could explore [Cygwin](http://www.cygwin.com/), which bills itself as "a
collection of tools which provide a Linux look and feel environment for
Windows," but I think that's stupid. Instead, I'm going to talk about the
terminal program that actually comes with Windows. It's called PowerShell. It's
powerful, but filled with weird, hyphenated commands that look completely alien
to a Linux user.

### Windows PowerShell

The fact is, PowerShell actually has a lot of cool features. I think the first
thing you need to know about PowerShell (after locating it on the start menu) is
where your "profile" script resides.

#### PowerShell Profile Location

The profile script gets called every time you load up PowerShell. If you're
familiar with Unix, you can think of this as the equivalent to
**$HOME/.bashrc**. (If you're not familiar,
[read this](http://www.faqs.org/docs/abs/HTML/files.html).)

Its location is exposed through the $profile variable in PowerShell.

You type:

    PS C:\ $profile

Out comes:

    C:\Users\YourName\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1

Pretty cool. But wait!

    PS C:\ type $profile
    Get-Content : Cannot find path 'C:\Users\YourName\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1' because it does not exist.

Oh. So go create it (which may involve creating the subdirectory
WindowsPowerShell). I'm sure there's a way to change all this, but for my
purposes, not necessary.

#### PowerShell Profile Variables

So, what do you put in the PowerShell profile? Here's what I've got in mine:

An extension of my current path, like so:

```ps1
$env:Path += ";C:\Paths\To\Add;C:\Separated By\Semicolons;F:\Etc\Etc\You Get\it"
```

A quick command to drop me where I want to be:

```ps1
Set-Location "C:\General\Working\Directory"
```

You can create aliases to save keystrokes or define entire functions. For
instance, I like to run IPython Notebook. Adding this to your $profile script

```ps1
function ipy { Invoke-Expression -Command "ipython.bat notebook --pylab inline" }
```

Makes this launch IPython Notebook:

    PS C:\ ipy

#### PowerShell Script Errors

If you get an error message from PowerShell informing you that "execution of
scripts is disabled on this system," you may want to examine the answers on
[this page](http://stackoverflow.com/questions/4037939/powershell-execution-of-scripts-is-disabled-on-this-system).
I chose the set-executionpolicy unrestricted solution, but that's probably
insecure for some reason or another.

### Installing Ruby Gems

Once you've got the hang of the command line, you'll want to install Ruby Gems.
To do that, you should download the ZIP file on
[this page](http://rubygems.org/pages/download), decompress the file and then
run:

    PS C:\Path\to\files\ ruby setup.rb

From the decompressed folder.

### Installing a Text Editor

Next, you'll need a decent editor. If you've got one, feel free to skip this
section.

For a long time, my go-to editor in Windows was Notepad++. It's extensible,
powerful and free. And just about the ugliest thing I've ever seen.

Recently, I've become a big fan of [Sublime Text](http://www.sublimetext.com/).
It's clean, powerful and pretty. Though I've got no design ability, it's
important to me that my tools be pretty.

If you get Sublime Text, you'll want to launch it from the command line. To make
this as painless as possible, I recommend adding something like this to your
$profile script (the one we detailed above, for those of you who are skimming).
Obviously, you'll need to change the path as needed:

```ps1
function st { Invoke-Expression -Command "START 'C:\Program Files\Sublime Text 2\sublime_text.exe' '$args'" }
```

That works for me. There are a few kinks in the process (you may have some
trouble using the Build command in Sublime Text), but for the most part, this
will allow you -- from PowerShell -- to edit files thusly:

    PS C:\ st myfile.txt

### Git

You can get Git [here](http://git-scm.com/).

### Jekyll

Jekyll "is a simple, blog aware, static site generator," says its
[README](https://github.com/mojombo/jekyll). I'm not going to sit here and
trumpet its strengths, since this is literally the first thing I've used it to
make. I'm certainly no expert, though I did get it up and running.

First, you'll want to take a stab at installing Jekyll as painlessly as
possible. Try this:

    gem install jekyll

#### Errors Installing Jekyll: Developer Kit

If that throws some crazy errors about not having a developer kit in the path,
go back to the [Ruby Installer](http://rubyinstaller.org/downloads/) page,
scroll down a bit and download the proper development kit. You can figure out
which one is right for you by reading the section labeled "Which Development
Kit" on the upper-right.

Download and execute the file. It'll decompress to the folder it's in (most of
the important stuff will go in the _bin_ subdirectory). You'll want to run
**devkitvars.ps1** (or **devkitvars.bat**), both of which should be readily
available.

    PS C:\Path\to\devkit\ devkitvars.ps1

## Deploying Jekyll

As I said, I'm no Jekyll expert. The "basic structure" of a Jekyll folder is
described [here](https://github.com/mojombo/jekyll/wiki/usage).

I'm not going to get into too many specifics about how it works. There are a
[lot](https://learn.andrewmunsell.com/learn/jekyll-by-example/)
[of](http://jekyllbootstrap.com/)
[resources](http://net.tutsplus.com/tutorials/other/building-static-sites-with-jekyll/)
and
[tutorials](http://danielmcgraw.com/2011/04/14/The-Ultimate-Guide-To-Getting-Started-With-Jekyll-Part-1/)
available via a simple
[Google search](https://www.google.com/search?q=jekyll+tutorial).

Instead of covering that ground again, I'm going to conclude this post with a
few details about how I deployed Jekyll from my home computer to a webserver
using Git.

The process is quite straightforward. I've only been using Git for a few weeks,
which is proof that any idiot can figure this out.

Basically, here are the steps you need to follow to deploy using Git. This
assumes you've got access to a webhost with SSH and Git already installed.

### Creating a Git Repository

First, on your **local machine**, navigate to the root of your Jekyll project
and initialize a Git repository.

    PS C:\Your\jekyll\project\ git init

Next, add the \_site folder to the repository.

    PS C:\Your\jekyll\project\ git add _site

Now, commit the repository:

    PS C:\Your\jekyll\project\ git commit -m "Init commit."

Next, we're going to want to create a bare repository on the **server** where
you'll be hosting the site. SSH to your server and navigate to the place you
want to have the repository. Note that this does not (and maybe should not?) be
a publicly exposed location. In my case, I put it beneath the HTML root folder.

My server is a Linux box. Here's what I did:

    bash ~/domains/rob-barry.com$ mkdir repo.git
    bash ~/domains/rob-barry.com$ cd repo.git
    bash ~/domains/rob-barry.com/repo.git$ git --bare init

That should return with a message saying you've initialized a bare repository in
repo.git.

Now, because I actually followed
[these directions](http://qugstart.com/blog/ruby-and-rails/create-a-new-git-remote-repository-from-some-local-files-or-local-git-repository/),
I typed this:

    bash ~/domains/rob-barry.com/repo.git$ git config core.sharedrepository 1
    bash ~/domains/rob-barry.com/repo.git$ git config receive.denyNonFastforwards true

Now, hop back to your **local machine**. The easiest thing to do is to add this
new repository as a remote:

    PS C:\Your\jekyll\project\ git remote add origin ssh://username@yoursite.com/path/to/your/git/repo.git

And then push the repository to the new site:

    git push -u origin master

Now, we flip back to the **server**, navigate to our root HTML directory, and
clone the repo:

    bash ~/domains/rob-barry.com/html$ git clone ~/domains/rob-barry.com/repo.git

### Redirecting Using .htaccess

If you follow these steps, you'll wind up with a copy of your Jekyll website in
the /repo/_site subdirectory. That won't do, so you'll need to make a quick
tweak to .htaccess:

```apacheconf
RewriteEngine on
RewriteCond %{HTTP_HOST} ^(www.)?rob-barry.com$
RewriteCond %{REQUEST_URI} !^/repo/_site/
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ /repo/_site/$1
RewriteCond %{HTTP_HOST} ^(www.)?rob-barry.com$
RewriteRule ^(/)?$ repo/_site/index.html [L]
```

Obviously, you'll want to replace rob-barry.com with your information (and
/repo/_site/ if necessary). This may come as a shock, but it's totally possible
there's a better way to do this. I don't know.

### Adding Post-Receive Hook

Lastly, we want to set this up so every time we run a push from the local
machine to the server, it updates the live website. We do this by navigating to
our repo.git directory on the **server** and then doing this:

    bash ~/domains/rob-barry.com/repo.git/ cd hooks
    bash ~/domains/rob-barry.com/repo.git/hooks/ mv post-receive.sample post-receive

Now, edit post-receive to contain a line like this:

```bash
unset GIT_DIR && cd ~/rob-barry.com/html/repo && git pull
```

And finally, do this:

    bash ~/domains/rob-barry.com/repo.git/hooks/ chmod a+x post-receive

## Conclusion

From here, you can add a bunch of folders to your .gitignore file. For this
site, my .gitignore file looks like this:

    _includes/*
    _layouts/*
    _plugins/*
    _posts/*
    assets/*
    pages/*
    _config.yml
    index.html

Good luck. Please let me know how it goes.

**EDIT 4/24:** Added summary field.
