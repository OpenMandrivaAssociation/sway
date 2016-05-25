git clone https://github.com/SirCmpwn/sway.git
pushd sway
git archive --format=tar --prefix sway-0.5-$(date +%Y%m%d)/ HEAD | xz -vf > ../sway-0.5-$(date +%Y%m%d).tar.xz
popd
