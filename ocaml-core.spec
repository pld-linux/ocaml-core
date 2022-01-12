#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Industrial strength alternative to OCaml's standard library
Summary(pl.UTF-8):	Przemysłowy zamiennik biblioteki standardowej OCamla
Name:		ocaml-core
Version:	0.14.1
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/core/tags
Source0:	https://github.com/janestreet/core/archive/v%{version}/core-%{version}.tar.gz
# Source0-md5:	b11f58205953d84cedb0003efcdab231
URL:		https://github.com/janestreet/core
BuildRequires:	ocaml >= 1:4.08.0
BuildRequires:	ocaml-core_kernel-devel >= 0.14
BuildRequires:	ocaml-core_kernel-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-jst-config-devel >= 0.14
BuildRequires:	ocaml-jst-config-devel < 0.15
BuildRequires:	ocaml-ppx_jane-devel >= 0.14
BuildRequires:	ocaml-ppx_jane-devel < 0.15
BuildRequires:	ocaml-sexplib-devel >= 0.14
BuildRequires:	ocaml-sexplib-devel < 0.15
BuildRequires:	ocaml-spawn-devel >= 0.12
BuildRequires:	ocaml-timezone-devel >= 0.14
BuildRequires:	ocaml-timezone-devel < 0.15
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Core suite of libraries is an industrial strength alternative to
OCaml's standard library that was developed by Jane Street, the
largest industrial user of OCaml.

This package contains files needed to run bytecode executables using
core library.

%description -l pl.UTF-8
Zbiór bibliotek Core to przemysłowy zamiennik biblioteki standardowej
OCamla, tworzony przez Jane Street, największego przemysłowego
użytkownika OCamla.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki core.

%package devel
Summary:	Industrial strength alternative to OCaml's standard library - development part
Summary(pl.UTF-8):	Przemysłowy zamiennik biblioteki standardowej OCamla - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-core_kernel-devel >= 0.14
Requires:	ocaml-jst-config-devel >= 0.14
Requires:	ocaml-ppx_jane-devel >= 0.14
Requires:	ocaml-sexplib-devel >= 0.14
Requires:	ocaml-spawn-devel >= 0.12
Requires:	ocaml-timezone-devel >= 0.14

%description devel
This package contains files needed to develop OCaml programs using
core library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki core.

%prep
%setup -q -n core-%{version}

%build
dune build --release --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/core/*.ml
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/core/*/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/core

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md COPYRIGHT.txt INRIA-DISCLAIMER.txt LICENSE.md README.md THIRD-PARTY.txt
%attr(755,root,root) %{_bindir}/corebuild
%attr(755,root,root) %{_bindir}/coretop
%dir %{_libdir}/ocaml/core
%{_libdir}/ocaml/core/META
%{_libdir}/ocaml/core/*.cma
%dir %{_libdir}/ocaml/core/bigbuffer_blocking
%{_libdir}/ocaml/core/bigbuffer_blocking/*.cma
%dir %{_libdir}/ocaml/core/bigstring_unix
%{_libdir}/ocaml/core/bigstring_unix/*.cma
%dir %{_libdir}/ocaml/core/daemon
%{_libdir}/ocaml/core/daemon/*.cma
%dir %{_libdir}/ocaml/core/error_checking_mutex
%{_libdir}/ocaml/core/error_checking_mutex/*.cma
%dir %{_libdir}/ocaml/core/iobuf_unix
%{_libdir}/ocaml/core/iobuf_unix/*.cma
%dir %{_libdir}/ocaml/core/linux_ext
%{_libdir}/ocaml/core/linux_ext/*.cma
%dir %{_libdir}/ocaml/core/lock_file_blocking
%{_libdir}/ocaml/core/lock_file_blocking/*.cma
%dir %{_libdir}/ocaml/core/nano_mutex
%{_libdir}/ocaml/core/nano_mutex/*.cma
%dir %{_libdir}/ocaml/core/process_env
%{_libdir}/ocaml/core/process_env/*.cma
%dir %{_libdir}/ocaml/core/squeue
%{_libdir}/ocaml/core/squeue/*.cma
%dir %{_libdir}/ocaml/core/syslog
%{_libdir}/ocaml/core/syslog/*.cma
%dir %{_libdir}/ocaml/core/time_stamp_counter
%{_libdir}/ocaml/core/time_stamp_counter/*.cma
%dir %{_libdir}/ocaml/core/top
%{_libdir}/ocaml/core/top/*.cma
%dir %{_libdir}/ocaml/core/uuid
%{_libdir}/ocaml/core/uuid/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/core/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core/bigbuffer_blocking/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core/bigstring_unix/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core/daemon/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core/error_checking_mutex/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core/iobuf_unix/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core/linux_ext/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core/lock_file_blocking/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core/nano_mutex/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core/process_env/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core/squeue/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core/syslog/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core/time_stamp_counter/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/core/uuid/*.cmxs
%endif
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllbigstring_unix_stubs.so
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllcore_stubs.so
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllerror_checking_mutex_stubs.so
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlliobuf_unix_stubs.so
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllinux_ext_stubs.so
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllsyslog_stubs.so
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlltime_stamp_counter_stubs.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/core/libcore_stubs.a
%{_libdir}/ocaml/core/config.h
%{_libdir}/ocaml/core/socketaddr.h
%{_libdir}/ocaml/core/*.cmi
%{_libdir}/ocaml/core/*.cmt
%{_libdir}/ocaml/core/*.cmti
%{_libdir}/ocaml/core/*.mli
%{_libdir}/ocaml/core/bigbuffer_blocking/*.cmi
%{_libdir}/ocaml/core/bigbuffer_blocking/*.cmt
%{_libdir}/ocaml/core/bigbuffer_blocking/*.cmti
%{_libdir}/ocaml/core/bigbuffer_blocking/*.mli
%{_libdir}/ocaml/core/bigstring_unix/libbigstring_unix_stubs.a
%{_libdir}/ocaml/core/bigstring_unix/*.cmi
%{_libdir}/ocaml/core/bigstring_unix/*.cmt
%{_libdir}/ocaml/core/bigstring_unix/*.cmti
%{_libdir}/ocaml/core/bigstring_unix/*.mli
%{_libdir}/ocaml/core/daemon/*.cmi
%{_libdir}/ocaml/core/daemon/*.cmt
%{_libdir}/ocaml/core/daemon/*.cmti
%{_libdir}/ocaml/core/daemon/*.mli
%{_libdir}/ocaml/core/error_checking_mutex/liberror_checking_mutex_stubs.a
%{_libdir}/ocaml/core/error_checking_mutex/*.cmi
%{_libdir}/ocaml/core/error_checking_mutex/*.cmt
%{_libdir}/ocaml/core/error_checking_mutex/*.cmti
%{_libdir}/ocaml/core/error_checking_mutex/*.mli
%{_libdir}/ocaml/core/iobuf_unix/libiobuf_unix_stubs.a
%{_libdir}/ocaml/core/iobuf_unix/*.cmi
%{_libdir}/ocaml/core/iobuf_unix/*.cmt
%{_libdir}/ocaml/core/iobuf_unix/*.cmti
%{_libdir}/ocaml/core/iobuf_unix/*.mli
%{_libdir}/ocaml/core/linux_ext/liblinux_ext_stubs.a
%{_libdir}/ocaml/core/linux_ext/*.cmi
%{_libdir}/ocaml/core/linux_ext/*.cmt
%{_libdir}/ocaml/core/linux_ext/*.cmti
%{_libdir}/ocaml/core/linux_ext/*.mli
%{_libdir}/ocaml/core/lock_file_blocking/*.cmi
%{_libdir}/ocaml/core/lock_file_blocking/*.cmt
%{_libdir}/ocaml/core/lock_file_blocking/*.cmti
%{_libdir}/ocaml/core/lock_file_blocking/*.mli
%{_libdir}/ocaml/core/nano_mutex/*.cmi
%{_libdir}/ocaml/core/nano_mutex/*.cmt
%{_libdir}/ocaml/core/nano_mutex/*.cmti
%{_libdir}/ocaml/core/nano_mutex/*.mli
%{_libdir}/ocaml/core/process_env/*.cmi
%{_libdir}/ocaml/core/process_env/*.cmt
%{_libdir}/ocaml/core/process_env/*.cmti
%{_libdir}/ocaml/core/process_env/*.mli
%{_libdir}/ocaml/core/squeue/*.cmi
%{_libdir}/ocaml/core/squeue/*.cmt
%{_libdir}/ocaml/core/squeue/*.cmti
%{_libdir}/ocaml/core/squeue/*.mli
%{_libdir}/ocaml/core/syslog/libsyslog_stubs.a
%{_libdir}/ocaml/core/syslog/*.cmi
%{_libdir}/ocaml/core/syslog/*.cmt
%{_libdir}/ocaml/core/syslog/*.cmti
%{_libdir}/ocaml/core/syslog/*.mli
%{_libdir}/ocaml/core/time_stamp_counter/libtime_stamp_counter_stubs.a
%{_libdir}/ocaml/core/time_stamp_counter/*.cmi
%{_libdir}/ocaml/core/time_stamp_counter/*.cmt
%{_libdir}/ocaml/core/time_stamp_counter/*.cmti
%{_libdir}/ocaml/core/time_stamp_counter/*.mli
%{_libdir}/ocaml/core/top/*.cmi
%{_libdir}/ocaml/core/top/*.cmt
%{_libdir}/ocaml/core/uuid/*.cmi
%{_libdir}/ocaml/core/uuid/*.cmt
%{_libdir}/ocaml/core/uuid/*.cmti
%{_libdir}/ocaml/core/uuid/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/core/core.a
%{_libdir}/ocaml/core/*.cmx
%{_libdir}/ocaml/core/*.cmxa
%{_libdir}/ocaml/core/bigbuffer_blocking/bigbuffer_blocking.a
%{_libdir}/ocaml/core/bigbuffer_blocking/*.cmx
%{_libdir}/ocaml/core/bigbuffer_blocking/*.cmxa
%{_libdir}/ocaml/core/bigstring_unix/bigstring_unix.a
%{_libdir}/ocaml/core/bigstring_unix/*.cmx
%{_libdir}/ocaml/core/bigstring_unix/*.cmxa
%{_libdir}/ocaml/core/daemon/daemon.a
%{_libdir}/ocaml/core/daemon/*.cmx
%{_libdir}/ocaml/core/daemon/*.cmxa
%{_libdir}/ocaml/core/error_checking_mutex/error_checking_mutex.a
%{_libdir}/ocaml/core/error_checking_mutex/*.cmx
%{_libdir}/ocaml/core/error_checking_mutex/*.cmxa
%{_libdir}/ocaml/core/iobuf_unix/iobuf_unix.a
%{_libdir}/ocaml/core/iobuf_unix/*.cmx
%{_libdir}/ocaml/core/iobuf_unix/*.cmxa
%{_libdir}/ocaml/core/linux_ext/linux_ext.a
%{_libdir}/ocaml/core/linux_ext/*.cmx
%{_libdir}/ocaml/core/linux_ext/*.cmxa
%{_libdir}/ocaml/core/lock_file_blocking/lock_file_blocking.a
%{_libdir}/ocaml/core/lock_file_blocking/*.cmx
%{_libdir}/ocaml/core/lock_file_blocking/*.cmxa
%{_libdir}/ocaml/core/nano_mutex/nano_mutex.a
%{_libdir}/ocaml/core/nano_mutex/*.cmx
%{_libdir}/ocaml/core/nano_mutex/*.cmxa
%{_libdir}/ocaml/core/process_env/process_env.a
%{_libdir}/ocaml/core/process_env/*.cmx
%{_libdir}/ocaml/core/process_env/*.cmxa
%{_libdir}/ocaml/core/squeue/squeue.a
%{_libdir}/ocaml/core/squeue/*.cmx
%{_libdir}/ocaml/core/squeue/*.cmxa
%{_libdir}/ocaml/core/syslog/syslog.a
%{_libdir}/ocaml/core/syslog/*.cmx
%{_libdir}/ocaml/core/syslog/*.cmxa
%{_libdir}/ocaml/core/time_stamp_counter/time_stamp_counter.a
%{_libdir}/ocaml/core/time_stamp_counter/*.cmx
%{_libdir}/ocaml/core/time_stamp_counter/*.cmxa
%{_libdir}/ocaml/core/uuid/uuid_unix.a
%{_libdir}/ocaml/core/uuid/*.cmx
%{_libdir}/ocaml/core/uuid/*.cmxa
%endif
%{_libdir}/ocaml/core/dune-package
%{_libdir}/ocaml/core/opam
