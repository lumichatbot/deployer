# -*- mode: ruby -*-
# vi: set ft=ruby :

$init = <<SCRIPT
  sudo DEBIAN_FRONTEND=noninteractive add-apt-repository ppa:avsm/ppa
  sudo DEBIAN_FRONTEND=noninteractive add-apt-repository ppa:ansible/bubblewrap
  sudo apt-get update
  sudo DEBIAN_FRONTEND=noninteractive apt-get full-upgrade -y
  sudo DEBIAN_FRONTEND=noninteractive apt-get install -y python3-pip
  sudo pip3 install pipenv

  sudo DEBIAN_FRONTEND=noninteractive apt-get install -y curl opam m4 \
    ocaml ocaml-native-compilers libmenhir-ocaml-dev software-properties-common \
    bubblewrap
  opam init
  eval $(opam config env)
  opam switch install 4.03.0
  eval $(opam config env)
  opam install -y ocamlfind oasis core \
     fieldslib cmdliner cstruct async_extended \
     async_parallel menhir sexplib sedlex ppx_import \
     ulex ipaddr tcpip base64 cohttp yojson \
     mparser ocamlgraph quickcheck ounit dune \
     cohttp-async cppo cstruct-async cstruct-sexp menhir \
     cppo menhir open ppx_deriving
  eval $(opam config env)
SCRIPT

$mininet = <<SCRIPT
  DEBIAN_FRONTEND=noninteractive sudo apt-get install -y mininet
SCRIPT

$ryu = <<SCRIPT
  sudo pip3 install zipp==1.0.0 ryu
SCRIPT

$dprle = <<SCRIPT
  git clone https://github.com/frenetic-lang/dprle.git
  pushd dprle
  sudo make
  sudo make install
  popd
SCRIPT

$frenetic = <<SCRIPT
  git clone https://github.com/frenetic-lang/frenetic.git
  # git checkout bbfbc36fd9b11162133e0921bcd1e86b29cf65c0
  pushd frenetic
  sudo make
  sudo make install
  popd
SCRIPT

$merlin = <<SCRIPT
  git clone https://github.com/merlin-lang/merlin.git
  pushd merlin
  make
  make test
  popd
SCRIPT

$lumi = <<SCRIPT
  pushd deployer
  pipenv install
  popd
SCRIPT

$cleanup = <<SCRIPT
  apt-get clean
  rm -rf /tmp/*
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-16.04"
  config.vm.define "lumi-deployer"

  config.vm.synced_folder ".", "/home/vagrant/deployer/"

  config.vm.provider "virtualbox" do |v|
      v.customize ["modifyvm", :id, "--cpuexecutioncap", "50"]
      v.customize ["modifyvm", :id, "--memory", "2048"]
  end

  ## Guest config
  config.vm.hostname = "lumi-deployer"
  config.vm.network :private_network, ip: "192.168.0.100"

  ## Provisioning
  config.vm.provision :shell, privileged: false, :inline => $init
  config.vm.provision :shell, privileged: false, :inline => $mininet
  config.vm.provision :shell, privileged: false, :inline => $ryu
  config.vm.provision :shell, privileged: false, :inline => $dprle
  config.vm.provision :shell, privileged: false, :inline => $frenetic
  # config.vm.provision :shell, privileged: false, :inline => $merlin
  config.vm.provision :shell, privileged: false, :inline => $lumi
  config.vm.provision :shell, :inline => $cleanup
end
