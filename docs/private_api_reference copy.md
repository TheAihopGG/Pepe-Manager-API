# Private API Reference

## Types of resources

### Package

```json
{
    "id": "...",
    "name": "...",
    "description": "...",
    "author_name": "...",
    "version": "...",
    "data": "...",
    "created_at": "...",
    "updated_at": "...",
}
```
### PackageInfo

`PackageInfo` is a `Package`, but without `data` property

```json
{
    "id": "...",
    "name": "...",
    "description": "...",
    "author_name": "...",
    "version": "...",
    "created_at": "...",
    "updated_at": "...",
}
```

## Urls

All urls are relative `<domain>://private/api`

> [!NOTE]
> Only domains from `configuration["allowed_domains"]` are allowed

### Create Package

|Method|Url|Description|
|------|---|-----------|
|GET|`/packages/create`|Creates a package|

Request:
```json
{
    "name": "...",
    "description": "...",
    "author_name": "...",
    "version": "...",
    "data": "...",
}
```

### Delete Package

|Method|Url|Description|
|------|---|-----------|
|GET|`/packages/delete`|Deletes a package|

Request:
```json
{
    "id": "...",
}
```

### Update package

|Method|Url|Description|
|------|---|-----------|
|GET|`/packages/update`|Updates a package|

Request:
```json
{
    "id": "...", // the ID of the updated package
    "name": "...", // all parameters are optional except id
    "description": "...",
    "author_name": "...",
    "version": "...",
    "data": "...",
}
```

> [!WARNING]
> You must specify at least one parameter

### Get Package

|Method|Url|Description|
|------|---|-----------|
|GET|`/packages/package`|Returns a package|

Request:
```json
{
    "package_id": "<id>"
}
```

Response:
```json
{
    "id": "...",
    "name": "...",
    "description": "...",
    "author_name": "...",
    "version": "...",
    "data": "...",
    "created_at": "...",
    "updated_at": "...",
}
```

### Get Package Info

|Method|Url|Description|
|------|---|-----------|
|GET|`/packages/package_info`|Returns a package|

Request:
```json
{
    "package_id": "<id>"
}
```

Response:
```json
{
    "id": "...",
    "name": "...",
    "description": "...",
    "author_name": "...",
    "version": "...",
    "created_at": "...",
    "updated_at": "...",
}
```

> [!NOTE]
> `PackageInfo` does not contain `data` property
