# Create the file /tmp/school with the content "I love Puppet"
file { '/tmp/school/school':
  ensure  => 'file',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
}
