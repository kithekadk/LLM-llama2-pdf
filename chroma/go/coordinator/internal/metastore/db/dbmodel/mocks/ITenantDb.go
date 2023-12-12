// Code generated by mockery v2.33.3. DO NOT EDIT.

package mocks

import (
	dbmodel "github.com/chroma/chroma-coordinator/internal/metastore/db/dbmodel"
	mock "github.com/stretchr/testify/mock"
)

// ITenantDb is an autogenerated mock type for the ITenantDb type
type ITenantDb struct {
	mock.Mock
}

// DeleteAll provides a mock function with given fields:
func (_m *ITenantDb) DeleteAll() error {
	ret := _m.Called()

	var r0 error
	if rf, ok := ret.Get(0).(func() error); ok {
		r0 = rf()
	} else {
		r0 = ret.Error(0)
	}

	return r0
}

// GetAllTenants provides a mock function with given fields:
func (_m *ITenantDb) GetAllTenants() ([]*dbmodel.Tenant, error) {
	ret := _m.Called()

	var r0 []*dbmodel.Tenant
	var r1 error
	if rf, ok := ret.Get(0).(func() ([]*dbmodel.Tenant, error)); ok {
		return rf()
	}
	if rf, ok := ret.Get(0).(func() []*dbmodel.Tenant); ok {
		r0 = rf()
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).([]*dbmodel.Tenant)
		}
	}

	if rf, ok := ret.Get(1).(func() error); ok {
		r1 = rf()
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// GetTenants provides a mock function with given fields: tenantID
func (_m *ITenantDb) GetTenants(tenantID string) ([]*dbmodel.Tenant, error) {
	ret := _m.Called(tenantID)

	var r0 []*dbmodel.Tenant
	var r1 error
	if rf, ok := ret.Get(0).(func(string) ([]*dbmodel.Tenant, error)); ok {
		return rf(tenantID)
	}
	if rf, ok := ret.Get(0).(func(string) []*dbmodel.Tenant); ok {
		r0 = rf(tenantID)
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).([]*dbmodel.Tenant)
		}
	}

	if rf, ok := ret.Get(1).(func(string) error); ok {
		r1 = rf(tenantID)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}

// Insert provides a mock function with given fields: in
func (_m *ITenantDb) Insert(in *dbmodel.Tenant) error {
	ret := _m.Called(in)

	var r0 error
	if rf, ok := ret.Get(0).(func(*dbmodel.Tenant) error); ok {
		r0 = rf(in)
	} else {
		r0 = ret.Error(0)
	}

	return r0
}

// NewITenantDb creates a new instance of ITenantDb. It also registers a testing interface on the mock and a cleanup function to assert the mocks expectations.
// The first argument is typically a *testing.T value.
func NewITenantDb(t interface {
	mock.TestingT
	Cleanup(func())
}) *ITenantDb {
	mock := &ITenantDb{}
	mock.Mock.Test(t)

	t.Cleanup(func() { mock.AssertExpectations(t) })

	return mock
}
