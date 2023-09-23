# This manifest installs flask package 2.1.0 from pip3.

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
