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
|POST|`/packages/create`|Creates a package|

Request:
```json
{
    "package_name": "...",
    "package_description": "...",
    "package_author_name": "...",
    "package_version": "...",
    "package_data": "...",
}
```

### Delete Package

|Method|Url|Description|
|------|---|-----------|
|DELETE|`/packages/delete`|Deletes a package|

Request:
```json
{
    "package_id": "...",
}
```

### Update package

|Method|Url|Description|
|------|---|-----------|
|PUT|`/packages/update`|Updates a package|

Request:
```json
{
    "package_id": "...", // the ID of the updated package
    "package_name": "...", // all parameters are optional except id
    "package_description": "...",
    "package_author_name": "...",
    "package_version": "...",
    "package_data": "...",
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
    "package_id": "...",
    "package_name": "...",
    "package_description": "...",
    "package_author_name": "...",
    "package_version": "...",
    "package_data": "...",
    "package_created_at": "...",
    "package_updated_at": "...",
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
    "package_id": "...",
    "package_name": "...",
    "package_description": "...",
    "package_author_name": "...",
    "package_version": "...",
    "package_created_at": "...",
    "package_updated_at": "...",
}
```

> [!NOTE]
> `PackageInfo` does not contain `data` property

### Get Packages Infos

|Method|Url|Description|
|------|---|-----------|
|GET|`/packages/packages_infos`|Returns packages with name|

Request:
```json
{
    "package_name": "<name>"
}
```

Response:
```json
[
    {
        "package_id": "...",
        "package_name": "...",
        "package_description": "...",
        "package_author_name": "...",
        "package_version": "...",
        "package_created_at": "...",
        "package_updated_at": "...",
    },
    {
        "package_id": "...",
        "package_name": "...",
        "package_description": "...",
        "package_author_name": "...",
        "package_version": "...",
        "package_created_at": "...",
        "package_updated_at": "...",
    },
    {
        "package_id": "...",
        "package_name": "...",
        "package_description": "...",
        "package_author_name": "...",
        "package_version": "...",
        "package_created_at": "...",
        "package_updated_at": "...",
    }
]
```
