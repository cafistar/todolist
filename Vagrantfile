# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "base"

  config.vm.define :vtodo do |vtodo|
    vtodo.vm.box = "bento/ubuntu-18.04"
    vtodo.vm.box_version = "202002.04.0"
    vtodo.vm.hostname = "todo"
    vtodo.vm.network :private_network, ip: "192.168.33.10"
    vtodo.vm.network :forwarded_port, guest: 80, host: 8000, host_ip: "127.0.0.1"
    vtodo.vm.network :forwarded_port, guest: 30, host: 3000, host_ip: "127.0.0.1"
    vtodo.vm.box_check_update = false
    vtodo.vm.synced_folder "./source", "/home/vagrant/source"
    vtodo.vm.provider "virtualbox" do |v|
        v.customize ["modifyvm", :id, "--memory", 2048, "--cpus", "1", "--ioapic", "off"]
    end
  end
end
