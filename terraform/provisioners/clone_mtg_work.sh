git init mtg_price
cd mtg_price/
git remote add -f origin git@github.com:brbcoffee/mtg_price.git
git config core.sparseCheckout true
echo "work" >> .git/info/sparse-checkout
git pull origin master