git merge master
rm -rf docs
npm run build
mv _book docs
git add .
git commit -m 'build'
git push
git co master
git push