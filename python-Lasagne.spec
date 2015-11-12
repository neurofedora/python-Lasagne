%global modname Lasagne

Name:           python-%{modname}
Version:        0.1
Release:        1%{?dist}
Summary:        Lightweight library to build and train neural networks in Theano

License:        MIT
URL:            http://lasagne.readthedocs.org/
Source0:        https://github.com/Lasagne/Lasagne/archive/v%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
Lasagne is a lightweight library to build and train neural networks in Theano.
Its main features are:
* Supports feed-forward networks such as Convolutional Neural Networks (CNNs),
  recurrent networks including Long Short-Term Memory (LSTM), and any
  combination thereof
* Allows architectures of multiple inputs and multiple outputs, including
  auxiliary classifiers
* Many optimization methods including Nesterov momentum, RMSprop and ADAM
* Freely definable cost function and no need to derive gradients due to Theano's
  symbolic differentiation
* Transparent support of CPUs and GPUs due to Theano's expression compiler

Its design is governed by six principles:
* Simplicity: Be easy to use, easy to understand and easy to extend, to
  facilitate use in research
* Transparency: Do not hide Theano behind abstractions, directly process and
  return Theano expressions or Python / numpy data types
* Modularity: Allow all parts (layers, regularizers, optimizers, ...) to be used
  independently of Lasagne
* Pragmatism: Make common use cases easy, do not overrate uncommon cases
* Restraint: Do not obstruct users with features they decide not to use
* Focus: "Do one thing and do it well"

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
%{?python_provide:%python_provide python2-lasagne}
BuildRequires:  python2-devel python2-setuptools
BuildRequires:  numpy
BuildRequires:  python-theano
# Test deps
BuildRequires:  python2-pytest python-mock
Requires:       numpy
Requires:       python-theano

%description -n python2-%{modname}
Lasagne is a lightweight library to build and train neural networks in Theano.
Its main features are:
* Supports feed-forward networks such as Convolutional Neural Networks (CNNs),
  recurrent networks including Long Short-Term Memory (LSTM), and any
  combination thereof
* Allows architectures of multiple inputs and multiple outputs, including
  auxiliary classifiers
* Many optimization methods including Nesterov momentum, RMSprop and ADAM
* Freely definable cost function and no need to derive gradients due to Theano's
  symbolic differentiation
* Transparent support of CPUs and GPUs due to Theano's expression compiler

Its design is governed by six principles:
* Simplicity: Be easy to use, easy to understand and easy to extend, to
  facilitate use in research
* Transparency: Do not hide Theano behind abstractions, directly process and
  return Theano expressions or Python / numpy data types
* Modularity: Allow all parts (layers, regularizers, optimizers, ...) to be used
  independently of Lasagne
* Pragmatism: Make common use cases easy, do not overrate uncommon cases
* Restraint: Do not obstruct users with features they decide not to use
* Focus: "Do one thing and do it well"

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
%{?python_provide:%python_provide python3-lasagne}
BuildRequires:  python3-devel python3-setuptools
BuildRequires:  python3-numpy
BuildRequires:  python3-theano
# Test deps
BuildRequires:  python3-pytest python3-mock
Requires:       python3-numpy
Requires:       python3-theano

%description -n python3-%{modname}
Lasagne is a lightweight library to build and train neural networks in Theano.
Its main features are:
* Supports feed-forward networks such as Convolutional Neural Networks (CNNs),
  recurrent networks including Long Short-Term Memory (LSTM), and any
  combination thereof
* Allows architectures of multiple inputs and multiple outputs, including
  auxiliary classifiers
* Many optimization methods including Nesterov momentum, RMSprop and ADAM
* Freely definable cost function and no need to derive gradients due to Theano's
  symbolic differentiation
* Transparent support of CPUs and GPUs due to Theano's expression compiler

Its design is governed by six principles:
* Simplicity: Be easy to use, easy to understand and easy to extend, to
  facilitate use in research
* Transparency: Do not hide Theano behind abstractions, directly process and
  return Theano expressions or Python / numpy data types
* Modularity: Allow all parts (layers, regularizers, optimizers, ...) to be used
  independently of Lasagne
* Pragmatism: Make common use cases easy, do not overrate uncommon cases
* Restraint: Do not obstruct users with features they decide not to use
* Focus: "Do one thing and do it well"

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}
# drop coverage and pep8 tests for py.test
sed -i -e '/pep8/d' -e '/cov/d' setup.cfg

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python2_sitelib} py.test-%{python2_version} -v
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -v

%files -n python2-%{modname}
%license LICENSE
%doc examples CHANGES.rst README.rst
%{python2_sitelib}/%{modname}*.egg-info
%{python2_sitelib}/lasagne/

%files -n python3-%{modname}
%license LICENSE
%doc examples CHANGES.rst README.rst
%{python3_sitelib}/%{modname}*.egg-info
%{python3_sitelib}/lasagne/

%changelog
* Thu Nov 12 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.1-1
- Initial package
